import re
from time import time, sleep

import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from exceptions import FailStep
from utils.tools import close_popups


class __Base:
    def __init__(self, browser):
        self._browser = browser


class Authorization(__Base):
    @allure.step('Authorization to the Application as {1} successful')
    def login(self, name, username):
        self._browser.get_by_name(name).send_keys(username)

    @allure.step('Full password field')
    def password(self, name, password):
        self._browser.get_by_name(name).send_keys(password)

    @allure.step('Click Login button')
    def click_log_in(self, id ):
        self._browser.get_by_id(id).click()

    @allure.step('Click Lost username or password button')
    def lost_password(self, name):
        self._browser.get_by_name(name).click()


class Deauthorization(__Base):

    # start of Changes by Paridhi
    # -------------------------------------------------------------------------
    @allure.step('Click on Toggle Menu')
    def click_menu(self):
        self._browser.get_by_id('action-menu-toggle-0').click()

    @allure.step('Click on logout')
    def click_logout(self):
        self._browser.get_by_id('actionmenuaction-5').click()

    # end of Changes by Paridhi
    # -------------------------------------------------------------------------


class Steps(__Base):

    # -------------------------------------------------------------------------
    # Author: Paridhi

    # methods for Add New User
    @allure.step('Get Page Title')
    def get_page_title(self):
        return self._browser.title

    @allure.step('Select GEAR')
    def find_gear(self):
        self._browser.get_by_css('#quickaccess-popover-container > div > span.flex-icon.ft-fw.ft.fa-cog').click()

    @allure.step('Select USER')
    def find_Users_button(self):
        self._browser.get_by_link('Users').click()

    @allure.step('Create User Button')
    def find_create_user(self):
        self._browser.get_by_css('.singlebutton:nth-child(4) input:nth-child(1)').click()

    @allure.step('Select and Enter Value')
    def find_elements_by_id_input(self, id, key_value):
        self._browser.get_by_id(id).send_keys(key_value)

    @allure.step('Click on Checkbox')
    def find_elements_checkbox(self, id):
        self._browser.get_by_id(id).click()

    @allure.step('Select and Click')
    def find_elements_by_id_click(self, id):
        self._browser.get_by_id(id).click()

    # methods for deleting the user
    @allure.step('Delete User')
    def click_on_delete_action(self, name):
        title = 'Delete ' + name
        self._browser.get_by_xpath(f'//*[@title="{title}"]').click()

    @allure.step('Confirm Delete User')
    def confirm_delete_learner(self):
        self._browser.get_by_css(
            '#modal-footer > div > div:nth-child(1) > form > div > input.form-submit.btn-primary').click()

    # methods for enrolling the user
    @allure.step('Select Course')
    def select_course(self, title):
        self._browser.get_by_xpath(f'//*[@title="{title}"]').click()

    @allure.step('Go to Course')
    def go_to_course(self):
        self._browser.get_by_css('a.tw-catalogDetails__manageLink').click()

    @allure.step('Enrol User')
    def go_to_enrol_user(self):
        self._browser.get_by_css('.type_unknown:nth-child(8) > .tree_item > span:nth-child(2)').click()

    @allure.step('Click on Enrolled Users')
    def click_enrolled_users(self):
        self._browser.get_by_link('Enrolled users').click()

    @allure.step('Click on Searched User')
    def click_on_user(self):
        self._browser.get_by_xpath('//div/div[3]/div[2]').click()

    @allure.step('Click on Enrol button')
    def click_on_enrol_button(self):
        self._browser.get_by_xpath('//div/div[4]/input').click()

    # methods for messaging test cases
    @allure.step('Click on message button')
    def click_on_message_button(self):
        self._browser.get_by_css('#nav-message-popover-container > div.popover-region-toggle.nav-link').click()

    @allure.step('Click on New Message')
    def click_new_message(self):
        self._browser.get_by_link('New message').click()

    @allure.step('Select user to send message')
    def go_to_searched_user_for_message(self):
        self._browser.get_by_xpath('//div[2]/div[2]/p').click()

    @allure.step('Write message')
    def go_to_write_message(self, message):
        self._browser.get_by_xpath('//div[1]/div[1]/textarea').send_keys(message)

    @allure.step('Click Send button')
    def click_send_button(self):
        self._browser.get_by_css(' div.send-button-container > button').click()

    # methods for Add new category test case
    @allure.step('Select Courses and categories')
    def find_course_category_link(self):
        self._browser.get_by_link('Courses and categories').click()

    @allure.step('Select Courses and categories')
    def find_create_new_category(self):
        self._browser.get_by_link('Create new category').click()

    # methods for Add a new program test case
    @allure.step('Select Programs')
    def find_program_link(self):
        self._browser.get_by_link('Programs').click()

    @allure.step('Click on Add a new program')
    def click_add_a_new_program(self):
        self._browser.get_by_css(
            '#region-main > div > div:nth-child(5) > div > form > div > input[type=submit]:nth-child(1)').click()

    # methods for Edit Category test case
    @allure.step('Click Gear to edit category')
    def click_gear_edit_category(self):
        self._browser.get_by_css('#action-menu-toggle-8 .fa-caret-down').click()

    @allure.step('Click Edit option')
    def click_edit_option_category(self):
        self._browser.get_by_css('#actionmenuaction-86').click()

    @allure.step('Click Cancel button')
    def click_cancel_button(self):
        self._browser.get_by_css('input#id_cancel.btn-cancel').click()

    # methods for Add a subcategory test case
    @allure.step('Click on Add a subcategory')
    def click_add_a_subcategory(self):
        self._browser.get_by_css(
            '#region-main > div > div.buttons > div:nth-child(1) > form > div > input[type=submit]:nth-child(1)').click()

    # methods for Permission test case
    @allure.step('Click on User Option')
    def click_administration_users(self):
        self._browser.get_by_css(
            '#frontpagesettings_group > li:nth-child(3) > p').click()

    @allure.step('Click on Permissions')
    def click_permissions(self):
        self._browser.get_by_link('Permissions').click()

    # methods for Assign Roles test case
    @allure.step('Click on Assigned roles')
    def click_assigned_roles(self):
        self._browser.get_by_link('Assigned roles').click()

    @allure.step('Click on Site Manager')
    def click_site_manager(self):
        self._browser.get_by_link('Site Manager').click()

    # methods for Audience test case
    @allure.step('Click on Audiences')
    def find_audiences_link(self):
        self._browser.get_by_link('Audiences').click()

    # methods for creating a new Audience test case
    @allure.step('Click on add a new Audiences')
    def click_add_new_audience_tab(self):
        self._browser.get_by_css('div.tabtree > ul > li:nth-child(3) > a').click()

    @allure.step('Enter Audience Name')
    def enter_audience_name(self, key_value):
        self._browser.get_by_id('id_name').send_keys(key_value)

    @allure.step('Change Audience type to Dynamic')
    def change_type_to_dynamic(self):
        self._browser.get_by_id('id_cohorttype').click()
        self._browser.get_by_css('#id_cohorttype > option:nth-child(2)').click()

    @allure.step('Click on Save Changes')
    def click_save_new_audience(self):
        self._browser.get_by_id('id_submitbutton').click()

    # methods for Delete Audience test case
    @allure.step('Click on desired Audience')
    def click_automated_audience(self):
        self._browser.get_by_link('Automated_audience').click()

    @allure.step('Click on delete this Audience button')
    def click_delete_audience_button(self):
        self._browser.get_by_css(
            '#region-main > div > div:nth-child(9) > form > div > input[type=submit]:nth-child(1)').click()

    @allure.step('Click on Yes to Confirm Deletion')
    def click_yes_to_delete_audience(self):
        self._browser.get_by_css(
            '#modal-footer > div > div:nth-child(1) > form > div > input.form-submit.btn-primary').click()

    # methods for adding a rule set for Audience test case
    @allure.step('Click on Rule Set tab')
    def click_rule_set_tab(self):
        self._browser.get_by_css('#region-main > div > div.tabtree > ul > li:nth-child(3) > a').click()

    @allure.step('Select Email from dropdown')
    def select_email_from_dropdown(self):
        self._browser.get_by_css('#id_addrulesetmenu > optgroup:nth-child(2) > option:nth-child(3)').click()

    @allure.step('Enter rule')
    def enter_rule(self):
        self._browser.get_by_css('input#id_listofvalues').send_keys('test')

    @allure.step('Save Rule')
    def save_rule(self):
        self._browser.get_by_css(
            'div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span').click()

    @allure.step('Approve Changes')
    def approve_changes(self):
        self._browser.get_by_css(
            '#cohort_rules_action_box > form > p:nth-child(3) > input[type=submit]:nth-child(1)').click()

    # methods for Audience Global settings test case
    @allure.step('Click on Audience Global settings')
    def click_audience_global_settings(self):
        self._browser.get_by_css(
            '#inst2 > div.content.block-content > ul > li:nth-child(2) > p > a > span.item-content-wrap').click()

    # methods for uploading Audience test case
    @allure.step('Click on Upload Audiences')
    def click_upload_audience_tab(self):
        self._browser.get_by_css('div.tabtree > ul > li:nth-child(4) > a').click()

    # methods for editing Audience test case
    @allure.step('Click Edit Details tab')
    def click_edit_details_tab(self):
        self._browser.get_by_css('#region-main > div > div.tabtree > ul > li:nth-child(2) > a').click()

    # methods for All Certifications test case
    @allure.step('Click All Certifications tab')
    def click_all_certifications_tab(self):
        self._browser.get_by_css('div.tabtree > ul > li:nth-child(3) > a').click()

    # methods for Other Evidence test case
    @allure.step('Click Other Evidence tab')
    def click_other_evidence_tab(self):
        self._browser.get_by_css('div.tabtree > ul > li:nth-child(2) > a').click()

    # methods for Active Courses test case
    @allure.step('Click Active Courses')
    def click_on_active_learning(self):
        self._browser.get_by_link('Active Learning').click()

    # methods for Completed Courses test case
    @allure.step('Click Completed Courses')
    def click_on_completed_learning(self):
        self._browser.get_by_link('Completed Learning').click()

    # methods for Manage Plans test case
    @allure.step('Click on Manage Plans')
    def click_on_manage_plans(self):
        self._browser.get_by_link('Manage plans').click()

    @allure.step('Click on Create a new learning plan')
    def click_on_create_new_learning_plan(self):
        self._browser.get_by_css('#dp-plans-description > div > form > input[type=submit]:nth-child(2)').click()

    @allure.step('Provide Plan Name')
    def provide_plan_name(self):
        self._browser.get_by_css('#id_name').clear()
        self._browser.get_by_css('#id_name').send_keys('Automated Learning Plan')

    @allure.step('Click on Create Plan Button')
    def click_create_plan_button(self):
        self._browser.get_by_css('input#id_submitbutton').click()

    @allure.step('Activate Learning Plan')
    def activate_learning_plan(self):
        self._browser.get_by_css('#yui_3_17_2_1_1583250250337_218').click()

    # methods for Add a new badge test case
    @allure.step('Click on course title')
    def click_on_course_title(self):
        self._browser.get_by_link('Financial Literacy Series').click()

    @allure.step('Click on Badges')
    def click_on_badge_option(self):
        self._browser.get_by_css('li:nth-child(14) > p > span:nth-child(2)').click()

    @allure.step('Click on Add a new badge')
    def click_on_add_a_new_badge(self):
        self._browser.get_by_link('Add a new badge').click()

    @allure.step('Click on Choose a file')
    def click_on_choose_a_file(self):
        self._browser.get_by_name('imagechoose').click()

    @allure.step('select the image')
    def select_image_locally(self):
        self._browser.get_by_name('repo_upload_file').send_keys('/Users/paridhisaxena/Downloads/hammerhead_squaare.png')

    @allure.step('Click upload this file button')
    def click_upload_this_file(self):
        self._browser.get_by_css('button.fp-upload-btn.btn-primary.btn').click()

    @allure.step('Enter the Badge Name')
    def enter_badge_name(self):
        self._browser.get_by_id('id_name').send_keys('Automated Badge')

    @allure.step('Enter the Badge Description')
    def enter_badge_description(self):
        self._browser.get_by_id('id_description').send_keys(
            'This badge is created by the Automation Script. It should get deleted soon!')

    @allure.step('Enter the Badge Description')
    def click_create_badge_button(self):
        self._browser.get_by_id('id_submitbutton').click()

    # methods for Manage Badges test case
    @allure.step('Click on manage badges')
    def click_on_manage_badges(self):
        self._browser.get_by_link('Manage badges').click()

    # methods for Manage Badges test case
    @allure.step('Click on x to delete badge')
    def click_on_x_delete_badge(self):
        self._browser.get_by_css('span.flex-icon.ft-fw.ft.fa-times.ft-state-danger').click()

    @allure.step('Confirm Badge deletion by choosing option 1')
    def confirm_delete_badge_option_1(self):
        self._browser.get_by_css(
            '#region-main > div > div:nth-child(3) > div > form > div > input[type=submit]:nth-child(1)').click()

    # methods for Create new course test case
    @allure.step('Click on category name')
    def click_on_category_name(self):
        self._browser.get_by_link('Automated_category').click()

    @allure.step('Click on create new course')
    def click_on_create_new_course(self):
        self._browser.get_by_css('div.listing-actions.course-listing-actions > a').click()

    @allure.step('Enter Course full name')
    def enter_course_fullname(self):
        self._browser.get_by_id('id_fullname').send_keys('Automated Course')

    @allure.step('Enter Course short name')
    def enter_course_shortname(self):
        self._browser.get_by_id('id_shortname').send_keys('Automated Course')

    @allure.step('Click Save and return button')
    def click_save_and_return(self):
        self._browser.get_by_id('id_saveandreturn').click()

    # methods for Upload Scorm Package to a Course test case
    @allure.step('Click on course name link')
    def click_on_course_name_link(self):
        self._browser.get_by_link('Automated Course').click()

    @allure.step('Click on course view')
    def click_on_course_view(self):
        self._browser.get_by_link('View').click()

    @allure.step('Click on Turn editing on button')
    def click_on_turn_editing_on(self):
        self._browser.get_by_css(
            '#page-navbar > div.breadcrumb-button > div > form > div > input[type=submit]:nth-child(1)').click()

    @allure.step('Click on topic 1 name')
    def click_topic_name(self):
        self._browser.get_by_xpath('//li[2]/div[3]/h3/span/span/a/span/span').click()

    @allure.step('Change topic 1 name')
    def change_topic_name(self):
        self._browser.get_by_xpath('//span/input').send_keys(Keys.CLEAR)
        self._browser.get_by_xpath('//span/input').send_keys('Temp Topic')
        self._browser.get_by_xpath('//span/input').send_keys(Keys.RETURN)

    @allure.step('Click on add activity')
    def click_on_add_activity(self):
        self._browser.get_by_xpath('(//a[contains(@href, \'#\')])[16]').click()

    @allure.step('Select SCORM activity')
    def select_scorm_activity(self):
        self._browser.get_by_css('input#item_scorm').click()

    @allure.step('Click on Add button')
    def click_on_add_button(self):
        self._browser.get_by_css('input.submitbutton').click()

    @allure.step('Enter Name to the package')
    def enter_name_to_package(self):
        self._browser.get_by_id('id_name').send_keys('Test Automation')

    @allure.step('Click on Add package')
    def click_add_package(self):
        self._browser.get_by_xpath(
            '//form/fieldset[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/a/span[1]/span[2]').click()

    @allure.step('select the scorm package locally')
    def select_scorm_package_locally(self):
        self._browser.get_by_name(
            'repo_upload_file').send_keys('/Users/paridhisaxena/Downloads/everyone_is_a_leader_test.zip')

    @allure.step('Enter the Course Description')
    def enter_course_description(self):
        self._browser.get_by_id('id_introeditoreditable').send_keys(
            'This course is created by the Automation Script. It should get deleted soon!')

    @allure.step('Click Save and return to course button')
    def click_save_and_return_to_course(self):
        self._browser.get_by_id('id_submitbutton2').click()

    # methods for Delete the Scorm Package test case
    @allure.step('Click action menu against course')
    def click_action_menu_course(self):
        self._browser.get_by_id('action-menu-10-menubar').click()

    @allure.step('Select delete option')
    def select_delete_option(self):
        self._browser.get_by_id('actionmenuaction-52').click()

    @allure.step('click yes to confirm deletion')
    def click_yes_to_delete(self):
        self._browser.get_by_xpath('//div[2]/div/div[2]/input').click()

    # methods for Check course completions test case
    @allure.step('Click on Check course completions')
    def click_check_course_completions(self):
        self._browser.get_by_link('Check course completions').click()

    # methods for Manage category test case
    @allure.step('Click on Manage category')
    def click_manage_category_link(self):
        self._browser.get_by_xpath('//div[2]/ul/li/ul/li[1]/p/a').click()

    # methods for Delete the Course test case
    @allure.step('Click on course delete')
    def click_on_course_delete(self):
        self._browser.get_by_link('Delete').click()

    @allure.step('Click on confirm course delete')
    def click_on_confirm_delete(self):
        self._browser.get_by_css(
            '#modal-footer > div > div:nth-child(1) > form > div > input.form-submit.btn-primary').click()

    # end of Changes by Paridhi
    # -------------------------------------------------------------------------
