"""
Author: Paridhi Saxena
Date: 1/30/2020
Suite: Login
This test suite focuses on login with valid credentials;
Login with invalid credentials; Lost username or password.
"""

from time import sleep
import pytest

login_url = 'https://testurl.com/'
admin_username = 'admintest'
admin_password = '5trnGer!'


@pytest.allure.story('Login Page > Login with a valid credentials / C989')
@pytest.mark.test_01
def test_qata_01(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)


@pytest.allure.story('Login Page > Login with invalid credentials / C964')
@pytest.mark.test_03
def test_qata_02(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)


@pytest.allure.story('Login Page > Lost username or password / C962')
@pytest.mark.test_03
def test_qata_03(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('LXP Landing page', frontend.driver)

    frontend.open_url('https://testurl.com/login/forgot_password.php')
    # frontend.authorization.lost_password('Lost username or password')
