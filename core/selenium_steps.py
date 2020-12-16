from core.frontend import *
from logger import logger


class Frontend:
    def __init__(self, browser, l, p):
        print('I am in selenium_steps: Frontent Class init')
        self._browser, self.login, self.passwd = browser, l, p

        self.refresh, self.back, self.forward = self.driver.refresh, self.driver.back, self.driver.forward

        self.authorization = Authorization(browser)
        # Changes by Paridhi
        # -------------------------------------------------------------------------
        self.deauthorization = Deauthorization(browser)
        self.step = Steps(browser)
        # end of Changes by Paridhi
        # -------------------------------------------------------------------------
        self.__steps = Steps(browser)
        self.open_url = self._browser.open_url
        logger.debug('frontend build completed')

    def __getattr__(self, item):
        # TODO: for debug
        sleep(.5)
        return getattr(self.__steps, item)

    @property
    def driver(self):
        return self._browser.driver
