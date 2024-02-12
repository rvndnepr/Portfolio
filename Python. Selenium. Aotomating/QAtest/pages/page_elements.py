from random import randint
import requests
from selenium.webdriver.common.by import By
from generator.data_generator import generate_user_data
from generator.data_generator import generate_person_data
from pages.base_page import BasePage
import time
# from data.user_data import UserData


class TextBoxPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    # def fill_text_box_page_fields(self):
    #     full_name = (By.CSS_SELECTOR, '#userName')
    #     e_mail = (By.CSS_SELECTOR, '#userEmail')
    #     current_address = (By.CSS_SELECTOR, '#currentAddress')
    #     permanent_address = (By.CSS_SELECTOR, '#permanentAddress')
    #     submit = (By.CSS_SELECTOR, '#submit')
    #     self.element_is_visible(full_name).send_keys(UserData.data_user_name)
    #     self.element_is_visible(e_mail).send_keys(UserData.data_user_email)
    #     self.element_is_visible(current_address).send_keys(UserData.data_user_cur_address)
    #     self.element_is_visible(permanent_address).send_keys(UserData.data_user_perm_address)
    #     self.element_is_visible(submit).click()

    def fill_text_box_page_fields(self):
        gen_user_data = generate_user_data()
        full_name = (By.CSS_SELECTOR, '#userName')
        e_mail = (By.CSS_SELECTOR, '#userEmail')
        current_address = (By.CSS_SELECTOR, 'textarea[id=currentAddress]')
        permanent_address = (By.CSS_SELECTOR, 'textarea[id=permanentAddress]')
        submit = (By.CSS_SELECTOR, '#submit')
        # self.element_is_visible(full_name).send_keys(gen_user_data.gen_name)
        self.send_keys_to(full_name, gen_user_data.gen_name)
        # self.element_is_visible(e_mail).send_keys(gen_user_data.gen_email)
        self.send_keys_to(e_mail, gen_user_data.gen_email)
        # self.element_is_visible(current_address).send_keys(gen_user_data.gen_cur_addr)
        self.send_keys_to(current_address, gen_user_data.gen_cur_addr)
        # self.element_is_visible(permanent_address).send_keys(gen_user_data.gen_perm_addr)
        self.send_keys_to(permanent_address, gen_user_data.gen_perm_addr)
        # self.element_is_visible(submit).click()
        self.click_on(submit)
        print(gen_user_data.gen_name, gen_user_data.gen_email, gen_user_data.gen_cur_addr, gen_user_data.gen_perm_addr)
        return gen_user_data

    def check_output_form(self):
        created_full_name = (By.CSS_SELECTOR, '#output #name')
        created_e_mail = (By.CSS_SELECTOR, '#output #email')
        created_cur_address = (By.CSS_SELECTOR, '#output #currentAddress')
        created_perm_address = (By.CSS_SELECTOR, '#output #permanentAddress')
        full_name_text = self.element_is_present(created_full_name).text.split(':')[1]
        e_mail_text = self.element_is_present(created_e_mail).text.split(':')[1]
        cur_address_text = self.element_is_present(created_cur_address).text.split(':')[1]
        perm_address_text = self.element_is_present(created_perm_address).text.split(':')[1]
        print(full_name_text, e_mail_text, cur_address_text, perm_address_text)
        return full_name_text, e_mail_text, cur_address_text, perm_address_text

    def go_to_checkbox_page(self):
        checkbox_page_button = (By.XPATH, "//div[@class='element-group'][1]//li[@class='btn btn-light '][1]")
        self.element_is_present(checkbox_page_button).click()


class CheckboxPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def open_full_list(self):
        expand_all_button = (By.CSS_SELECTOR, "button[title='Expand all']")
        # self.element_is_visible(expand_all_button).click()
        self.click_on(expand_all_button)

    def click_any_checkbox(self):
        elements_list = (By.CSS_SELECTOR, "span[class='rct-title']")
        elements_list_text = self.elements_are_visible(elements_list)
        element = elements_list_text[randint(1, 15)]
        self.move_to_element(element)
        element.click()

    # def click_any_checkbox(self):
    #     elements_list = (By.CSS_SELECTOR, "span[class='rct-title']")
    #     elements_list_text = self.elements_are_visible(elements_list)
    #     count = 15
    #     while count != 0:
    #         element = elements_list_text[randint(1, 16)]
    #         if count > 0:
    #             self.move_to_element(element)
    #             element.click()
    #             count -= 1
    #         else:
    #             break

    # def get_checked_checkboxes(self):
    #     checked_elements = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    #     self.elements_are_present(checked_elements)
    #     title = (".//ancestor::span[@class='rct-title']")
    #     data = []
    #     for i in checked_elements:
    #         title_element = i.find_element_by_xpath(title)
    #         data.append(title_element.text)
    #     print(data)
    #     return data

    def get_checked_checkboxes(self):
        checked_items = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
        checked_list = self.elements_are_present(checked_items)
        item_title = ".//ancestor::span[@class='rct-text']"
        data = []
        for item in checked_list:
            item_text = item.find_element(By.XPATH, item_title)
            data.append(item_text.text)
            # print(title_item_text.text)
        # print(data)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_elements(self):
        output_elements = (By.CSS_SELECTOR, "span[class='text-success']")
        output_list = self.elements_are_present(output_elements)
        # item_title = ".//ancestor::span[@class='rct-text']"
        output_text = []
        for item in output_list:
            # item_text = item.find_element(By.XPATH, item_title)
            output_text.append(item.text)
        # print(output_text)
        return str(output_text).replace(' ', '').lower()

    def collapse_full_list(self):
        collapse_all_button = (By.CSS_SELECTOR, "button[title='Collapse all']")
        # self.element_is_visible(collapse_all_button).click()
        self.click_on(collapse_all_button)

    def go_to_radio_buttons_page(self):
        web_radio_buttons_page_button = (By.XPATH, "//div[@class='element-group'][1]//li[@class='btn btn-light '][2]")
        self.element_is_present(web_radio_buttons_page_button).click()


class RadioButtonPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def click_any_radio_button(self):
        value = ['yesRadio', 'impressiveRadio']
        random_value = randint(0, len(value) - 1)
        radio_btn = (By.XPATH, f"//label[@for='{value[random_value]}']")
        self.element_is_visible(radio_btn).click()
        time.sleep(1)
        element_text = self.element_is_visible(radio_btn).text
        return element_text

    # def get_output_result(self):
    #     output_text = {By.CSS_SELECTOR, "span[class='text-success']"}
    #     time.sleep(1)
    #     element_text = self.element_is_present(output_text)
    #     return element_text.text

    def go_to_web_tables_page(self):
        web_tables_page_button = (By.XPATH, "//div[@class='element-group'][1]//li[@class='btn btn-light '][3]")
        self.element_is_present(web_tables_page_button).click()

    # def click_any_radio_button(self, choice):
    #     yes_radio_button = (By.CSS_SELECTOR, "label[class*='custom-control'][for='yesRadio']")
    #     impressive_radio_button = (By.CSS_SELECTOR, "label[class*='custom-control'][for='impressiveRadio']")
    #     # no_radio_button = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    #     choices = {"Yes": yes_radio_button,
    #                "Impressive": impressive_radio_button,
    #                # "No": no_radio_button
    #                }
    #     self.element_is_visible(choices[choice]).click()
    #     time.sleep(1)
    #
    # def get_output_result(self):
    #     time.sleep(1)
    #     output_result = {By.CSS_SELECTOR, "span[class='text-success']"}
    #     return self.element_is_present(output_result).text


class WebTablesPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def add_new_person(self):
        time.sleep(1)
        add_user_btn = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
        self.element_is_visible(add_user_btn).click()

    # def fill_person_form(self):
    #     person = generate_person_data()
    #     person_first_name_input = (By.CSS_SELECTOR, "input[id='firstName']")
    #     person_last_name_input = (By.CSS_SELECTOR, "input[id='lastName")
    #     person_email_input = (By.CSS_SELECTOR, "input[id='userEmail")
    #     person_age_input = (By.CSS_SELECTOR, "input[id='age']")
    #     person_salary_input = (By.CSS_SELECTOR, "input[id='salary']")
    #     person_department_input = (By.CSS_SELECTOR, "input[id='department']")
    #     submit_btn = (By.XPATH, "//button[@id='submit']")
    #     search_input = (By.CSS_SELECTOR, "input[id='searchBox']")
    #     self.send_keys_to(person_first_name_input, person.first_name)
    #     self.send_keys_to(person_last_name_input, person.last_name)
    #     self.send_keys_to(person_email_input, person.e_mail)
    #     self.send_keys_to(person_age_input, person.age)
    #     self.send_keys_to(person_salary_input, person.salary)
    #     self.send_keys_to(person_department_input, person.department)
    #     self.element_is_visible(submit_btn).click()
    #     time.sleep(0.5)
    #     self.send_keys_to(search_input, person.e_mail)
    #     print(person.first_name, person.last_name, person.e_mail, person.age, person.salary, person.department)
    #     return person

    def fill_person_form(self):
        count = 1
        while count != 0:
            person = generate_person_data()
            person_first_name_input = (By.CSS_SELECTOR, "input[id='firstName']")
            person_last_name_input = (By.CSS_SELECTOR, "input[id='lastName")
            person_age_input = (By.CSS_SELECTOR, "input[id='age']")
            person_email_input = (By.CSS_SELECTOR, "input[id='userEmail")
            person_salary_input = (By.CSS_SELECTOR, "input[id='salary']")
            person_department_input = (By.CSS_SELECTOR, "input[id='department']")
            submit_btn = (By.XPATH, "//button[@id='submit']")
            first_name = person.first_name
            last_name = person.last_name
            age = person.age
            e_mail = person.e_mail
            salary = person.salary
            department = person.department
            self.element_is_visible(person_first_name_input).send_keys(first_name)
            self.element_is_visible(person_last_name_input).send_keys(last_name)
            self.element_is_visible(person_age_input).send_keys(age)
            self.element_is_visible(person_email_input).send_keys(e_mail)
            self.element_is_visible(person_salary_input).send_keys(salary)
            self.element_is_visible(person_department_input).send_keys(department)
            self.element_is_visible(submit_btn).click()
            count -= 1
            return [first_name, last_name, age, e_mail, salary, department]

    def get_added_person_data(self):
        user_data_list = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
        result_list = self.elements_are_present(user_data_list)
        result_text = []
        for item in result_list:
            result_text.append(item.text.splitlines())
        return result_text

    def search_person(self, key_word):
        time.sleep(1)
        search_input = (By.CSS_SELECTOR, "input[id='searchBox']")
        self.element_is_visible(search_input).send_keys(key_word)

    def check_search_person(self):
        row_parent = (By.XPATH, "//div[@class='rt-tbody']")
        row = self.get_element_text(row_parent)
        return row.splitlines()

    # def check_search_person(self):
    #     delete_btn = (By.CSS_SELECTOR, "span[title='Delete']")
    #     row_parent = ".//ancestor::div[@class='rt-tr-group']"
    #     delete_button = self.element_is_present(delete_btn)
    #     row = delete_button.find_element(By.XPATH, row_parent)
    #     return row.text.splitlines()

    def update_person_info(self):
        person = generate_person_data()
        salary = person.salary
        update_person_data_btn = (By.CSS_SELECTOR, "span[title='Edit']")
        salary_input = (By.CSS_SELECTOR, "#salary")
        submit_btn = (By.CSS_SELECTOR, "#submit")
        self.element_is_visible(update_person_data_btn).click()
        self.element_is_visible(salary_input).clear()
        self.element_is_visible(salary_input).send_keys(salary)
        self.element_is_visible(submit_btn).click()
        return str(salary)

    def delete_added_person(self):
        delete_btn = (By.CSS_SELECTOR, "span[title='Delete']")
        self.element_is_visible(delete_btn).click()

    def check_person_deleted(self):
        no_rows_element = (By.CSS_SELECTOR, "div[class='rt-noData']")
        title = self.get_element_text(no_rows_element)
        return title

    def change_rows_count(self):
        value = [5, 10, 20, 25, 50, 100]
        random_value = randint(0, len(value) - 1)
        rows_select = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
        rows_count = (By.CSS_SELECTOR, f"option[value='{value[random_value]}']")
        rows_list = self.element_is_visible(rows_select)
        self.move_to_element(rows_list)
        self.element_is_present(rows_select).click()
        self.element_is_visible(rows_count).click()
        return value[random_value]

    def check_rows_count(self):
        rows_elements = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
        rows = self.elements_are_present(rows_elements)
        return len(rows)

    # def change_rows_count(self):
    #     rows_count = [5, 10, 20, 25, 50, 100]
    #     data = []
    #     for item in rows_count:
    #
    #     rows_list = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    #     add_rows_select = self.elements_are_visible(rows_list)
    #     element = add_rows_select[randint(0, 4)]
    #     time.sleep(2)
    #     self.move_to_element(element)
    #     element.click()

    def go_to_buttons_page(self):
        buttons_page_button = (By.XPATH, "//div[@class='element-group'][1]//li[@class='btn btn-light '][4]")
        self.element_is_present(buttons_page_button).click()


class ButtonsPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def click_on_double_click_buttons(self):
        double_click_btn = (By.CSS_SELECTOR, "#doubleClickBtn")
        double_click_result_element = (By.CSS_SELECTOR, "#doubleClickMessage")
        self.double_click_on(self.element_is_visible(double_click_btn))
        double_click_text = self.element_is_present(double_click_result_element).text
        return double_click_text

    def click_on_right_click_buttons(self):
        right_click_btn = (By.CSS_SELECTOR, "#rightClickBtn")
        right_click_result_element = (By.CSS_SELECTOR, "#rightClickMessage")
        self.right_button_click_on(self.element_is_visible(right_click_btn))
        right_click_text = self.element_is_present(right_click_result_element).text
        return right_click_text

    def click_on_simple_click_buttons(self):
        simple_click_btn = (By.XPATH, "//div[@class='mt-4'][2]//button[@class='btn btn-primary']")
        # In this construction below every 3rd element is selected
        # simple_click_btn = (By.CSS_SELECTOR, "div[class='mt-4']:nth-child(3n)")
        simple_click_result_element = (By.CSS_SELECTOR, "#dynamicClickMessage")
        self.element_is_visible(simple_click_btn).click()
        simple_click_text = self.element_is_present(simple_click_result_element).text
        return simple_click_text

    def go_to_links_page(self):
        links_page_button = (By.XPATH, "//div[@class='element-group'][1]//li[@class='btn btn-light '][5]")
        self.element_is_present(links_page_button).click()


class LinksPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def check_working_link(self):
        working_link = (By.CSS_SELECTOR, "a[id='simpleLink']")
        link = self.element_is_visible(working_link)
        link_href = link.get_attribute('href')
        request = requests.get(link_href)
        time.sleep(2)
        if request.status_code == 200:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        broken_link = (By.CSS_SELECTOR, "a[id='bad-request']")
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(broken_link).click()
        else:
            return request.status_code

    def go_to_broken_links_page(self):
        buttons_page_button = (By.XPATH, "//div[@class='element-group'][1]//li[@class='btn btn-light '][6]")
        self.element_is_present(buttons_page_button).click()
