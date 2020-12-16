"""
Author: Paridhi Saxena
Date: 1/30/2020
Suite: User Management
This test suite focuses on creating learner; deleting learner;
Enroll learner to a course and Send message to a learner.
"""

from time import sleep
import pytest

login_url = 'https://testurl.com/'
admin_username = 'admintest'
admin_password = '5trnGer!'
course_name = 'Covid Preventive Measures'


@pytest.allure.story('Add New User > Learner / C988')
@pytest.mark.test_02
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
    frontend.step.find_Users_button()
    log.attach_selenium_screenshot('Click User', frontend.driver)

    sleep(3)
    frontend.step.find_create_user()
    log.attach_selenium_screenshot('Click Create User', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_input('id_username', 'automated.user')
    log.attach_selenium_screenshot('Username', frontend.driver)

    sleep(3)
    frontend.step.find_elements_checkbox('id_createpassword')
    log.attach_selenium_screenshot('Generate Password', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_input('id_firstname', 'Automation')
    log.attach_selenium_screenshot('Enter Firstname', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_input('id_lastname', 'User')
    log.attach_selenium_screenshot('Enter Lastname', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_input('id_email', 'automated.user@test.com')
    log.attach_selenium_screenshot('Enter Lastname', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_click('id_submitbutton2')
    log.attach_selenium_screenshot('Click Save and go back button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Remove User / C998')
@pytest.mark.test_02
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
    frontend.step.find_Users_button()
    log.attach_selenium_screenshot('Click User', frontend.driver)

    sleep(3)
    frontend.step.click_on_delete_action('Automation User')
    log.attach_selenium_screenshot('Find User To Delete', frontend.driver)

    sleep(3)
    frontend.step.confirm_delete_learner()
    log.attach_selenium_screenshot('Confirm Delete', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Enrolled user to a Course / C999')
@pytest.mark.test_02
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
    frontend.step.find_elements_by_id_click('menuitem6')
    log.attach_selenium_screenshot('Click Find Learning', frontend.driver)

    sleep(3)
    frontend.step.select_course(course_name)
    log.attach_selenium_screenshot('Select Course', frontend.driver)

    sleep(3)
    frontend.step.go_to_course()
    log.attach_selenium_screenshot('Go to Course', frontend.driver)

    sleep(3)
    frontend.step.go_to_enrol_user()
    log.attach_selenium_screenshot('Users', frontend.driver)

    sleep(3)
    frontend.step.click_enrolled_users()
    log.attach_selenium_screenshot('Enrol User', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_click('enrolusersbutton-1')
    log.attach_selenium_screenshot('Click Enrol User Button', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_input('enrolusersearch', 'Todd')
    log.attach_selenium_screenshot('Search Enrol User', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_click('searchbtn')
    log.attach_selenium_screenshot('Click Search button', frontend.driver)

    sleep(3)
    frontend.step.click_on_user()
    log.attach_selenium_screenshot('Click on Searched User', frontend.driver)

    # TODO: investigate more efficient way to do this
    sleep(3)
    frontend.step.click_on_enrol_button()
    log.attach_selenium_screenshot('Click on enrol button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Sent message to a User / C1000')
@pytest.mark.test_02
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
    frontend.step.click_on_message_button()
    log.attach_selenium_screenshot('Click on Message Button', frontend.driver)

    sleep(3)
    frontend.step.click_new_message()
    log.attach_selenium_screenshot('Click on New Message', frontend.driver)

    sleep(3)
    frontend.step.find_elements_by_id_input('searchtext', 'Todd')
    log.attach_selenium_screenshot('Search Enrol User', frontend.driver)

    sleep(3)
    frontend.step.go_to_searched_user_for_message()
    log.attach_selenium_screenshot('Go to searched User', frontend.driver)

    sleep(3)
    frontend.step.go_to_write_message('This is automated message')
    log.attach_selenium_screenshot('Write message', frontend.driver)

    sleep(3)
    frontend.step.click_send_button()
    log.attach_selenium_screenshot('Click Send button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)
