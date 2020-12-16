"""
Author: Paridhi Saxena
Date: 2/17/2020
Suite: Manage Programs
This test suite focuses on adding new category; add a new program;
add a subcategory; permissions; assign roles; audiences.
"""


from time import sleep
import pytest

login_url = 'https://testurl.com/'
admin_username = 'admintest'
admin_password = '5trnGer!'
course_name = 'Covid Preventive Measures'


@pytest.allure.story('Add new category / C1012')
@pytest.mark.test_03
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


@pytest.allure.story('Add  a new program / C1013')
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

    sleep(3)
    frontend.step.find_gear()
    log.attach_selenium_screenshot('Click Gear', frontend.driver)

    sleep(3)
    frontend.step.find_program_link()
    log.attach_selenium_screenshot('Click Programs', frontend.driver)

    sleep(3)
    frontend.step.click_add_a_new_program()
    log.attach_selenium_screenshot('Click on Add a new program', frontend.driver)

    sleep(3)
    frontend.step.change_category_to_automated()
    log.attach_selenium_screenshot('Change the category', frontend.driver)

    sleep(3)
    frontend.step.save_changes_to_program()
    log.attach_selenium_screenshot('Save Changes to Program', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Edit category / C1015')
@pytest.mark.test_03
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
    frontend.step.click_gear_edit_category()
    log.attach_selenium_screenshot('Click Gear to edit category', frontend.driver)

    sleep(3)
    frontend.step.click_edit_option_category()
    log.attach_selenium_screenshot('Click Edit option', frontend.driver)

    sleep(3)
    frontend.step.click_cancel_button()
    log.attach_selenium_screenshot('Click Cancel button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Add a subcategory / C1017')
@pytest.mark.test_03
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
    frontend.step.click_add_a_subcategory()
    log.attach_selenium_screenshot('Click on Add a subcategory', frontend.driver)

    sleep(3)
    frontend.step.click_cancel_button()
    log.attach_selenium_screenshot('Click Cancel button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Permissions / C1018')
@pytest.mark.test_03
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
    frontend.step.click_administration_users()
    log.attach_selenium_screenshot('Click on User Option', frontend.driver)

    sleep(3)
    frontend.step.click_permissions()
    log.attach_selenium_screenshot('Click on Permissions', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Assign Roles / C1019')
@pytest.mark.test_03
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
    frontend.step.click_administration_users()
    log.attach_selenium_screenshot('Click on User Option', frontend.driver)

    sleep(3)
    frontend.step.click_permissions()
    log.attach_selenium_screenshot('Click on Permissions', frontend.driver)

    sleep(3)
    frontend.step.click_assigned_roles()
    log.attach_selenium_screenshot('Click on Assigned roles', frontend.driver)

    sleep(3)
    frontend.step.click_site_manager()
    log.attach_selenium_screenshot('Click on Site Manager', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Audiences / C1020')
@pytest.mark.test_03
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
    frontend.step.find_audiences_link()
    log.attach_selenium_screenshot('Click on Audiences', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Delete Program / C1133')
@pytest.mark.test_03
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
    frontend.step.find_program_link()
    log.attach_selenium_screenshot('Click Programs', frontend.driver)

    sleep(3)
    frontend.step.click_program_to_delete()
    log.attach_selenium_screenshot('Select the Program to be deleted', frontend.driver)

    sleep(3)
    frontend.step.click_x_to_delete_program()
    log.attach_selenium_screenshot('Click on x to delete Program', frontend.driver)

    sleep(3)
    frontend.step.click_continue_to_delete_program()
    log.attach_selenium_screenshot('Click on continue to confirm program deletion', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Delete Category / C1132')
@pytest.mark.test_03
def test_qata_09(log, frontend):
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
