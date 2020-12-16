"""
Author: Paridhi Saxena
Date: 2/25/2020
Suite: Badges
This test suite focuses on adding a new badge; managing badges;
and deleting badge.
"""


from time import sleep
import pytest

login_url = 'https://testurl.com/'
admin_username = 'admintest'
admin_password = '5trnGer!'
course_name = 'Covid Preventive Measures'


@pytest.allure.story('Add a new badge / C1047')
@pytest.mark.test_06
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
    frontend.step.find_elements_by_id_click('menuitem20')
    log.attach_selenium_screenshot('Click Record of Learning', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_title()
    log.attach_selenium_screenshot('Click on course title', frontend.driver)

    sleep(3)
    frontend.step.click_on_badge_option()
    log.attach_selenium_screenshot('Click on Badges', frontend.driver)

    sleep(3)
    frontend.step.click_on_add_a_new_badge()
    log.attach_selenium_screenshot('Click on Add a new badge', frontend.driver)

    sleep(3)
    frontend.step.enter_badge_name()
    log.attach_selenium_screenshot('Enter the Badge Name', frontend.driver)

    sleep(3)
    frontend.step.enter_badge_description()
    log.attach_selenium_screenshot('Enter the Badge Description', frontend.driver)

    sleep(3)
    frontend.step.click_on_choose_a_file()
    log.attach_selenium_screenshot('Click on Choose a file', frontend.driver)

    # Change the path of the image in the method to the image saved on local system
    sleep(3)
    frontend.step.select_image_locally()
    log.attach_selenium_screenshot('select the image', frontend.driver)

    sleep(3)
    frontend.step.click_upload_this_file()
    log.attach_selenium_screenshot('Click upload this file button', frontend.driver)
    sleep(3)

    sleep(3)
    frontend.step.click_create_badge_button()
    log.attach_selenium_screenshot('Click create badge button', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Manage badges / C1048')
@pytest.mark.test_06
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
    frontend.step.find_elements_by_id_click('menuitem20')
    log.attach_selenium_screenshot('Click Record of Learning', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_title()
    log.attach_selenium_screenshot('Click on course title', frontend.driver)

    sleep(3)
    frontend.step.click_on_badge_option()
    log.attach_selenium_screenshot('Click on Badges', frontend.driver)

    sleep(3)
    frontend.step.click_on_manage_badges()
    log.attach_selenium_screenshot('Click on manage badges', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Delete badge / C1135')
@pytest.mark.test_06
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
    frontend.step.find_elements_by_id_click('menuitem20')
    log.attach_selenium_screenshot('Click Record of Learning', frontend.driver)

    sleep(3)
    frontend.step.click_on_course_title()
    log.attach_selenium_screenshot('Click on course title', frontend.driver)

    sleep(3)
    frontend.step.click_on_badge_option()
    log.attach_selenium_screenshot('Click on Badges', frontend.driver)

    sleep(3)
    frontend.step.click_on_manage_badges()
    log.attach_selenium_screenshot('Click on manage badges', frontend.driver)

    sleep(3)
    frontend.step.click_on_x_delete_badge()
    log.attach_selenium_screenshot('Click on x to delete badge', frontend.driver)

    sleep(3)
    frontend.step.confirm_delete_badge_option_1()
    log.attach_selenium_screenshot('CConfirm Badge deletion by choosing option 1', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)
