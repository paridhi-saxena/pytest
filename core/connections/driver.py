import os
import re
import time
from json import dumps

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, \
    WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from exceptions import SeleniumWebDriverError, SeleniumBrowserNotStarting, SeleniumWebElementError
from logger import logger
from utils.tools import close_popups


class ReconnectForDriver:
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            for attempt in range(2, -1, -1):
                try:
                    close_popups(instance.driver)
                    print('Reconnect Instance is: {}'.format(instance))
                    self.method(instance, *args, **kwargs)
                    break

                except Exception as e:
                    # return instance
                    instance.status = 'restart'
                    logger.warning('Browser error %s' % instance.node_info, exc_info=e)
                    if instance.node_connect_retry_count:
                        instance.node_connect_retry_count -= 1
                        instance.restart_session()

            else:
                logger.fatal('Fatal error %s' % instance)
                raise SeleniumBrowserNotStarting()

        return wrapper


class ClosePopups:
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            print('ClosePopups Instance is: {}'.format(instance))
            close_popups(instance.driver)
            self.method(instance, *args, **kwargs)

        return wrapper


class SeleniumWebElement(WebElement):
    #
    __re_number = re.compile('^[+-]?[\d]*[.,]?\d+$')
    #
    __re_formatting = re.compile('^|\?|\n|\r|\t|\s|$')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timeout = int(os.getenv('SELENIUM_TIMEOUT', 10))
        self.__text = None

    # **************************************************************************************************************** #

    @property
    def text(self):
        if super().text:
            self.__text = re.sub('^|\n\?|\nselect|$', '', super().text)
        else:
            self.__text = re.sub('^|\?|\n|\r|\t|$', '', self.get_attribute("textContent")).strip()
        return self.__text

    @property
    def name(self):
        name = self.get_attribute("name")
        return name

    @property
    def disabled(self):
        get = self.get_attribute('disabled')

        # wrap for  disabled
        if get == 'true':
            get = 'inactive'

        elif not get or get == 'false':
            get = 'active'

        return get

    @property
    def required(self):
        return self.get_attribute('required')

    @property
    def value(self):
        # Extra helping functions
        def is_str_to_float(v):
            if self.__re_number.search(self.__re_formatting.sub('', v)):
                return True
            else:
                return False

        def str_to_float(v):
            return round(
                float(
                    self.__re_formatting.sub('', v.replace(',', '.'))
                ), 3
            )

        # List
        attribute_list = ('value',)

        # Tru to get attribute
        for atr in attribute_list:
            value = self.get_attribute(atr)
            if value:
                break
        else:
            value = self.text.strip()

        # Checking the value is not a check box
        if self.get_attribute('type') == 'checkbox':
            value = self.get_attribute('checked')
            return value if value else False

        else:
            # Reformat message.
            if is_str_to_float(value):
                return str_to_float(value)

            elif value == 'true':
                return True

            elif value == 'false':
                return False
            return value

    @property
    def class_web_element(self):
        return self.get_attribute('class')

    # **************************************************************************************************************** #

    def __web_element_wait__(self):
        time_start = time.time()
        while not (self.is_displayed() and self.is_enabled()):
            time.sleep(0.05)
            if (time.time() - time_start) > self.timeout:
                if not self.is_displayed():
                    raise SeleniumWebElementError(
                        'Element %s (%s) currently not displayed, after = %s' % (self.text, self.name, self.timeout)
                    )
                else:
                    raise SeleniumWebElementError(
                        'Element %s (%s) currently not enabled, after = %s' % (self.text, self.name, self.timeout)
                    )

    # **************************************************************************************************************** #

    def click(self, attempt=3):
        self.__web_element_wait__()
        # Amount of attempts
        error = None
        for _ in range(attempt):
            try:
                super().click()
                break
            except WebDriverException as e:
                logger.warning('Not possible to click')
                error = e
        else:
            raise error

    def send_keys(self, keys):
        self.__web_element_wait__()
        # Remove from validation
        for _ in range(5):
            self.clear()
            if not self.get_attribute('value'):
                break
            else:
                logger.warning('Not possible to clean ')
                time.sleep(.001)
        else:
            logger.fatal('Fatal Error: %r' % self.value)

        logger.debug('Value %r' % self.value)
        super().send_keys(keys)

    def clear(self):
        self.__web_element_wait__()
        super().clear()

    def get_attribute(self, name):
        try:
            get = super().get_attribute(name)
        except WebDriverException:
            get = None

        return get

    def pprint(self):
        return {
            'name': self.name,
            'text': self.text,
            'disabled': self.disabled,
            'enabled': self.is_enabled(),
            'size': self.size,
            'class': self.class_web_element
        }

    def print_property(self):
        return dict(
            disabled=self.disabled,
            **{'name': self.name} if self.name else {},
            **{'text': self.text} if self.text else {},
        )


class SeleniumWebDriver:
    # Get selenium driver
    # Information about session
    session_info = []
    # ИInformation about current windows
    window = {}
    cookies = None
    status = None

    def __init__(self, **kwargs):
        self.driver = None
        self.time_out = int(os.getenv('SELENIUM_TIMEOUT', 15))

        self.node_info = None
        self.node_connect_retry_count = int(os.getenv('SELENIUM_COUNT_RESTART_BROWSER', 10))

        self.__dict__.update(kwargs)
        self.start_session()
        self.attempt = 0

    def __str__(self):
        return dumps(
            {
                'session_info': self.session_info,
                'count_restart_node': self.node_connect_retry_count,
                'status': self.status
            },
            indent=4)

    def __prepare_window(self, url):
        self.delete_all_cookies()
        self.get_cookies()
        self.open_url(url)

    def start_session(self):
        # 3 attempts to get a nood
        print('I am creating a new session: start_session in driver.py')
        logger.info('Selenium: create new object driver(browser)')
        if os.getenv('USE_LOCALHOST', None) or getattr(self, 'local', None):
            self.driver = getattr(webdriver, self.browser_name)(
                self.path,
                desired_capabilities=self.capabilities
            )

        else:
            self.driver = webdriver.Remote(
                command_executor=self.grid,
                desired_capabilities=self.capabilities
            )
        print('Driver is: {}'.format(self.driver))
        #
        self.driver._web_element_cls = SeleniumWebElement

        # Set selenium driver parameters
        self.driver.set_script_timeout(15)

        # Get diagnostic info from selenium node and put it to STDOUT
        self.node_info = {
            'session_id': self.driver.session_id,
            'failed': False
        }
        self.driver.set_window_size(1920, 1080)
        # self.driver.maximize_window()

        self.status = 'started'
        self.window.update({'window': self.driver.window_handles[0]})
        self.session_info.append(self.node_info)
        logger.info('Session: %s' % self)

    # Full
    def restart_session(self):
        self.start_session()
        self.open_url(self.window['url'])

    def get_cookies(self):
        self.cookies = {v['name']: v['value'] for v in self.driver.get_cookies()}

    # clean cash
    @ReconnectForDriver
    def reload(self):
        self.status = 'clean'
        if self.status != 'started':
            logger.subdebug('Clean  %r с url %r' % (self.window['window'], self.window['url']))

            self.driver.switch_to_window(self.window['window'])
            self.driver.execute_script('window.localStorage.clear(); location.reload();')
            self.__prepare_window(self.window['url'])

        self.status = 'started'

    def logs(self):
        exclude_logs = [
        ]
        return [
            item['message'] for item in self.driver.get_log('browser')
            if any([log not in item['message'] for log in exclude_logs])
        ]

    # Selenium tools ###################################################################################################
    @ClosePopups
    def save_screenshot(self, save_path):
        # Get screenshot
        self.driver.save_screenshot(save_path)

    @ReconnectForDriver
    def delete_all_cookies(self):
        # Clear browser cookie
        self.driver.delete_all_cookies()

    def quit(self):
        # Close browser session
        self.driver.quit()

    @ReconnectForDriver
    def open_url(self, url):
        # Got to URL
        print('I am Print! Open url: %s' % url)
        logger.debug('Open url: %s' % url)
        self.driver.get(url)

    @property
    def current_url(self):
        # Get current url
        return self.driver.current_url

    @property
    def url(self):
        return self.window['url']

    # Elements getters #################################################################################################
    def _get_element(self, path_type, element_path, need_fail=True, custom_time_out=None, is_elements_list=False):
        """
        Get element
                :param path_type: locator part
                :param element_path: Path
                :param need_fail: Return value need_fail (None, False)
                :param custom_time_out: Time of element
                :param is_elements_list: Return list of elements
                :return:
        """

        __type = {
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'id': By.ID,
            'class': By.CLASS_NAME,
            'tag': By.TAG_NAME,
            'link': By.LINK_TEXT,
            'name': By.NAME
        }
        if custom_time_out is not None:
            time_out = custom_time_out
        else:
            time_out = self.time_out

        try:
            if not is_elements_list:
                #
                logger.debug('Get list of elements %r path %r' % (path_type, element_path))
                return WebDriverWait(self.driver, time_out).until(
                    expected_conditions.presence_of_element_located((__type.get(path_type), element_path))
                )
            else:
                logger.debug('Get list of elements %r path %r' % (path_type, element_path))
                return WebDriverWait(self.driver, time_out).until(
                    expected_conditions.presence_of_all_elements_located((__type.get(path_type), element_path))
                )

        except (TimeoutException, UnexpectedAlertPresentException):
            if need_fail:
                raise SeleniumWebDriverError('Cannot find element by %s: %r' % (path_type, element_path))
            else:
                if is_elements_list:
                    return list()
                else:
                    return need_fail

    def get_by_xpath(self, xpath, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by XPath
        return self._get_element('xpath', xpath, need_fail=need_fail, is_elements_list=is_elements_list,
                                 custom_time_out=custom_time_out)

    def get_by_css(self, css, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by CSS
        return self._get_element('css', css, need_fail=need_fail, is_elements_list=is_elements_list,
                                 custom_time_out=custom_time_out)

    def get_by_id(self, e_id, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by ID
        return self._get_element('id', e_id, need_fail=need_fail, is_elements_list=is_elements_list,
                                 custom_time_out=custom_time_out)

    def get_by_tag(self, tag, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by TAG
        return self._get_element('tag', tag, need_fail=need_fail, is_elements_list=is_elements_list,
                                 custom_time_out=custom_time_out)

    def get_by_name(self, name, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by NAME
        return self._get_element('name', name, need_fail=need_fail, is_elements_list=is_elements_list,
                                 custom_time_out=custom_time_out)

    def get_by_link(self, link, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by LINK TEXT
        return self._get_element('link', link, need_fail=need_fail, is_elements_list=is_elements_list,
                                 custom_time_out=custom_time_out)

    @ClosePopups
    def scroll(self, element_move):
        act = ActionChains(self.driver)
        # scroll to elements
        act.move_to_element(element_move).move_by_offset(10, 30)
        time.sleep(.5)
        # Show
        act.perform()
        time.sleep(.2)
