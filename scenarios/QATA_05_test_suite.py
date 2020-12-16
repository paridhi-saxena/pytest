"""
Author: Paridhi Saxena
Date: 2/25/2020
Suite: Record of Learning
This test suite focuses on All Courses; All Certifications; Other Evidences;
Active Courses; Completed Courses; Create Learning Plans; Delete Learning Plan.
"""


from time import sleep
import pytest

login_url = 'https://testurl.com/'
admin_username = 'admintest'
admin_password = '5trnGer!'
course_name = 'Covid Preventive Measures'


@pytest.allure.story('Record of Learning: All Courses / C1022')
@pytest.mark.test_05
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
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Record of Learning: All Certifications / C1023')
@pytest.mark.test_05
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
    frontend.step.click_all_certifications_tab()
    log.attach_selenium_screenshot('Click All Certifications tab', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Record of Learning: Other Evidence / C1024')
@pytest.mark.test_05
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
    frontend.step.click_other_evidence_tab()
    log.attach_selenium_screenshot('Click Other Evidence tab', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Record of Learning: Active Courses / C1025')
@pytest.mark.test_05
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
    frontend.step.find_elements_by_id_click('menuitem20')
    log.attach_selenium_screenshot('Click Record of Learning', frontend.driver)

    sleep(3)
    frontend.step.click_on_active_learning()
    log.attach_selenium_screenshot('Click Active Learning', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Record of Learning: Completed Courses / C1026')
@pytest.mark.test_05
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
    frontend.step.find_elements_by_id_click('menuitem20')
    log.attach_selenium_screenshot('Click Record of Learning', frontend.driver)

    sleep(3)
    frontend.step.click_on_completed_learning()
    log.attach_selenium_screenshot('Click Completed Courses', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_menu()
    log.attach_selenium_screenshot('Click on Toggle menu', frontend.driver)

    sleep(3)
    frontend.deauthorization.click_logout()
    log.attach_selenium_screenshot('Click on Logout option', frontend.driver)


@pytest.allure.story('Create Learning Plans / C1027')
@pytest.mark.test_05
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
    frontend.step.find_elements_by_id_click('menuitem20')
    log.attach_selenium_screenshot('Click Record of Learning', frontend.driver)

    sleep(3)
    frontend.step.click_on_manage_plans()
    log.attach_selenium_screenshot('Click on Manage Plans', frontend.driver)

    sleep(3)
    frontend.step.click_on_create_new_learning_plan()
    log.attach_selenium_screenshot('Click on Create a new learning plan', frontend.driver)

    sleep(3)
    frontend.step.provide_plan_name()
    log.attach_selenium_screenshot('Provide Plan Name', frontend.driver)

    sleep(5)
    frontend.step.click_create_plan_button()
    log.attach_selenium_screenshot('Click on Create Plan Button', frontend.driver)
    sleep(5)

    # TODO: unable to make the submit button click
    # sleep(5)
    # frontend.step.activate_learning_plan()
    # log.attach_selenium_screenshot('Activate Learning Plan', frontend.driver)


@pytest.allure.story('Delete Learning Plan / C1134')
@pytest.mark.test_05
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
    frontend.step.find_elements_by_id_click('menuitem20')
    log.attach_selenium_screenshot('Click Record of Learning', frontend.driver)

    sleep(3)
    frontend.step.click_on_manage_plans()
    log.attach_selenium_screenshot('Click on Manage Plans', frontend.driver)
    # TODO: complete this test case once test_qata_06 gets completed.
