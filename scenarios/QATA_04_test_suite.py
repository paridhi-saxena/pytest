"""
Author: Paridhi Saxena
Date: 2/24/2020
Suite: Audiences
This test suite focuses on creating new audience; audience global settings;
upload audiences; edit audiences; add a rule set; delete audiences.
"""


from time import sleep
import pytest

login_url = 'https://testurl.com/'
admin_username = 'admintest'
admin_password = '5trnGer!'
course_name = 'Covid Preventive Measures'


@pytest.allure.story('Create New Audience / C1021')
@pytest.mark.test_04
def test_qata_01(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)

    sleep(3)
    frontend.step.find_gear()
    log.attach_selenium_screenshot('Click Gear', frontend.driver)

    sleep(3)
    frontend.step.find_audiences_link()
    log.attach_selenium_screenshot('Click on Audiences', frontend.driver)

    sleep(3)
    frontend.step.click_add_new_audience_tab()
    log.attach_selenium_screenshot('Click on add a new Audiences', frontend.driver)

    sleep(3)
    frontend.step.enter_audience_name('Automated_audience')
    log.attach_selenium_screenshot('Enter Audience Name', frontend.driver)

    sleep(3)
    frontend.step.change_type_to_dynamic()
    log.attach_selenium_screenshot('Change Audience type to Dynamic', frontend.driver)

    sleep(3)
    frontend.step.click_save_new_audience()
    log.attach_selenium_screenshot('Click on Save Changes', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Audience global settings / C1057')
@pytest.mark.test_04
def test_qata_02(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)

    sleep(3)
    frontend.step.find_gear()
    log.attach_selenium_screenshot('Click Gear', frontend.driver)

    sleep(3)
    frontend.step.find_audiences_link()
    log.attach_selenium_screenshot('Click on Audiences', frontend.driver)

    sleep(3)
    frontend.step.click_audience_global_settings()
    log.attach_selenium_screenshot('Click on Audience Global settings', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Upload audiences / C1058')
@pytest.mark.test_04
def test_qata_03(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)

    sleep(3)
    frontend.step.find_gear()
    log.attach_selenium_screenshot('Click Gear', frontend.driver)

    sleep(3)
    frontend.step.find_audiences_link()
    log.attach_selenium_screenshot('Click on Audiences', frontend.driver)

    sleep(3)
    frontend.step.click_upload_audience_tab()
    log.attach_selenium_screenshot('Click on Upload Audiences', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Edit audience / C1059')
@pytest.mark.test_04
def test_qata_04(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)

    sleep(3)
    frontend.step.find_gear()
    log.attach_selenium_screenshot('Click Gear', frontend.driver)

    sleep(3)
    frontend.step.find_audiences_link()
    log.attach_selenium_screenshot('Click on Audiences', frontend.driver)

    sleep(3)
    frontend.step.click_automated_audience()
    log.attach_selenium_screenshot('Click on desired Audience', frontend.driver)

    sleep(3)
    frontend.step.click_edit_details_tab()
    log.attach_selenium_screenshot('Click Edit Details tab', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Add a Rule Set / C1060')
@pytest.mark.test_04
def test_qata_05(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)

    sleep(3)
    frontend.step.find_gear()
    log.attach_selenium_screenshot('Click Gear', frontend.driver)

    sleep(3)
    frontend.step.find_audiences_link()
    log.attach_selenium_screenshot('Click on Audiences', frontend.driver)

    sleep(3)
    frontend.step.click_automated_audience()
    log.attach_selenium_screenshot('Click on desired Audience', frontend.driver)

    sleep(3)
    frontend.step.click_rule_set_tab()
    log.attach_selenium_screenshot('Click on Rule Set tab', frontend.driver)

    sleep(3)
    frontend.step.select_email_from_dropdown()
    log.attach_selenium_screenshot('Select Email from dropdown', frontend.driver)

    sleep(3)
    frontend.step.enter_rule()
    log.attach_selenium_screenshot('Enter rule', frontend.driver)

    sleep(3)
    frontend.step.save_rule()
    log.attach_selenium_screenshot('Save Rule', frontend.driver)

    sleep(3)
    frontend.step.approve_changes()
    log.attach_selenium_screenshot('Approve Changes', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Delete Audience / C1131')
@pytest.mark.test_04
def test_qata_06(log, frontend):
    frontend.open_url(login_url)
    log.attach_selenium_screenshot('Landing page', frontend.driver)

    frontend.authorization.login('username', admin_username)
    log.attach_selenium_screenshot('Fill up username', frontend.driver)

    frontend.authorization.password('password', admin_password)
    log.attach_selenium_screenshot('Fill up correct password', frontend.driver)

    frontend.authorization.click_log_in('loginbtn')
    log.attach_selenium_screenshot('Click Login Button', frontend.driver)

    sleep(3)
    frontend.step.find_gear()
    log.attach_selenium_screenshot('Click Gear', frontend.driver)

    sleep(3)
    frontend.step.find_audiences_link()
    log.attach_selenium_screenshot('Click on Audiences', frontend.driver)

    sleep(3)
    frontend.step.click_automated_audience()
    log.attach_selenium_screenshot('Click on desired Audience', frontend.driver)

    sleep(3)
    frontend.step.click_delete_audience_button()
    log.attach_selenium_screenshot('Click on delete this Audience button', frontend.driver)

    sleep(3)
    frontend.step.click_yes_to_delete_audience()
    log.attach_selenium_screenshot('Click on Yes to Confirm Deletion', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)
