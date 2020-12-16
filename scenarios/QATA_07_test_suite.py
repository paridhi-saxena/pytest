"""
Author: Paridhi Saxena
Date: 3/10/2020
Suite: Course and Categories
This test suite focuses on creating new category; create new course;
Upload Scorm Package to a Course; Check course completions; Manage category;
Delete the Scorm Package; Delete the Course; Delete Category
"""

from time import sleep
import pytest

login_url = 'https://testurl.com/'
admin_username = 'admintest'
admin_password = '5trnGer!'
course_name = 'Covid Preventive Measures'


@pytest.allure.story('Create new category / C1049')
@pytest.mark.test_07
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.find_create_new_category()
    log.attach_selenium_screenshot('Click Create new category', frontend.driver)

    sleep(3)
    frontend.step.change_parent_category()
    log.attach_selenium_screenshot('Change Parent Category', frontend.driver)

    sleep(3)
    frontend.step.write_name_new_category()
    log.attach_selenium_screenshot('Provide name to Category', frontend.driver)

    sleep(3)
    frontend.step.click_save_category()
    log.attach_selenium_screenshot('Click Save to Category', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Create new course / C1050')
@pytest.mark.test_07
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.click_on_category_name()
    log.attach_selenium_screenshot('Click on category name', frontend.driver)

    sleep(3)
    frontend.step.click_on_create_new_course()
    log.attach_selenium_screenshot('Click on create new course', frontend.driver)

    sleep(3)
    frontend.step.enter_course_fullname()
    log.attach_selenium_screenshot('Enter Course full name', frontend.driver)

    sleep(3)
    frontend.step.enter_course_shortname()
    log.attach_selenium_screenshot('Enter Course short name', frontend.driver)

    sleep(3)
    frontend.step.click_save_and_return()
    log.attach_selenium_screenshot('Click Save and return button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Upload Scorm Package to a Course / C1107')
@pytest.mark.test_07
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.click_on_category_name()
    log.attach_selenium_screenshot('Click on category name', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_name_link()
    log.attach_selenium_screenshot('Click on course name link', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_view()
    log.attach_selenium_screenshot('Click on course view', frontend.driver)

    sleep(3)
    frontend.step.click_on_turn_editing_on()
    log.attach_selenium_screenshot('Click on Turn editing on button', frontend.driver)

    sleep(3)
    frontend.step.click_topic_name()
    log.attach_selenium_screenshot('Click on topic 1 name', frontend.driver)

    # TODO: renaming topic doesn't work at the moment.
    # sleep(5)
    # frontend.step.change_topic_name()
    # log.attach_selenium_screenshot('Change topic 1 name', frontend.driver)

    sleep(3)
    frontend.step.click_on_add_activity()
    log.attach_selenium_screenshot('Click on add activity', frontend.driver)

    sleep(3)
    frontend.step.select_scorm_activity()
    log.attach_selenium_screenshot('Select SCORM activity', frontend.driver)

    sleep(3)
    frontend.step.click_on_add_button()
    log.attach_selenium_screenshot('Click on Add button', frontend.driver)

    sleep(3)
    frontend.step.enter_name_to_package()
    log.attach_selenium_screenshot('Enter Name to the package', frontend.driver)

    sleep(3)
    frontend.step.click_add_package()
    log.attach_selenium_screenshot('Click on Add package', frontend.driver)

    sleep(3)
    frontend.step.select_scorm_package_locally()
    log.attach_selenium_screenshot('select the scorm package locally', frontend.driver)

    sleep(3)
    frontend.step.click_upload_this_file()
    log.attach_selenium_screenshot('Click upload this file button', frontend.driver)

    sleep(50)
    frontend.step.enter_course_description()
    log.attach_selenium_screenshot('Enter the Course Description', frontend.driver)

    sleep(3)
    frontend.step.click_save_and_return_to_course()
    log.attach_selenium_screenshot('Click Save and return to course button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Check course completions / C1052')
@pytest.mark.test_07
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.click_check_course_completions()
    log.attach_selenium_screenshot('Click on Check course completions', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Manage category / C1053')
@pytest.mark.test_07
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.click_manage_category_link()
    log.attach_selenium_screenshot('Click on Manage category', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Delete the Scorm Package / C1136')
@pytest.mark.test_07
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.click_on_category_name()
    log.attach_selenium_screenshot('Click on category name', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_name_link()
    log.attach_selenium_screenshot('Click on course name link', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_view()
    log.attach_selenium_screenshot('Click on course view', frontend.driver)

    sleep(3)
    frontend.step.click_on_turn_editing_on()
    log.attach_selenium_screenshot('Click on Turn editing on button', frontend.driver)

    sleep(3)
    frontend.step.click_action_menu_course()
    log.attach_selenium_screenshot('Click action menu against course', frontend.driver)

    sleep(3)
    frontend.step.select_delete_option()
    log.attach_selenium_screenshot('Select delete option', frontend.driver)

    sleep(3)
    frontend.step.click_yes_to_delete()
    log.attach_selenium_screenshot('click yes to confirm deletion', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Delete the Course / C1136')
@pytest.mark.test_07
def test_qata_07(log, frontend):
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.click_on_category_name()
    log.attach_selenium_screenshot('Click on category name', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_name_link()
    log.attach_selenium_screenshot('Click on course name link', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_delete()
    log.attach_selenium_screenshot('Click on course delete', frontend.driver)

    sleep(3)
    frontend.step.click_on_confirm_delete()
    log.attach_selenium_screenshot('Click on confirm course delete', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Delete Category / C1132')
@pytest.mark.test_07
def test_qata_08(log, frontend):
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
    frontend.step.find_course_category_link()
    log.attach_selenium_screenshot('Click Courses and categories', frontend.driver)

    sleep(3)
    frontend.step.click_gear_edit_category()
    log.attach_selenium_screenshot('Click Gear to edit category', frontend.driver)

    sleep(3)
    frontend.step.click_delete_option_category()
    log.attach_selenium_screenshot('Click Delete option', frontend.driver)

    sleep(3)
    frontend.step.click_delete_button()
    log.attach_selenium_screenshot('Click Delete button for category', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)
