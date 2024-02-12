import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from generator.data_generator import generate_user_data
# from data.user_data import UserData


class ModalsAndPopups(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_content_language_pop_up(self):
        ukr_lang_button = (By.CSS_SELECTOR, "button[class='btn btn-primary']")
        lang_popup_header = (By.XPATH, "//div[@class='modal modal-w-460 fade show']//h5[@class='modal-title']")
        lang_popup_text = self.element_is_present(lang_popup_header).text
        self.click_on(ukr_lang_button)
        return lang_popup_text

    def check_registration_module(self):
        random_user = generate_user_data()
        registration_btn = (By.XPATH, "//li[@class='nav-item'][2]//div[@class='comments-tabs__title']")
        user_last_name_input = (By.CSS_SELECTOR, "input[id='signupform-lastname']")
        user_first_name_input = (By.CSS_SELECTOR, "input[id='signupform-firstname']")
        user_middle_name_input = (By.CSS_SELECTOR, "input[id='signupform-middlename']")
        user_phone_input = (By.CSS_SELECTOR, "input[id='signupform-phone']")
        user_email_input = (By.CSS_SELECTOR, "input[id='signupform-email']")
        password_input = (By.CSS_SELECTOR, "input[id='signupform-password']")
        confirm_password_input = (By.CSS_SELECTOR, "input[id='signupform-password_confirm']")
        sign_up_btn = (By.XPATH, "//div[@id='authItem2']//button[@class='btn btn-secondary btn-md popup-form__btn']")
        last_name = random_user.last_name
        first_name = random_user.first_name
        middle_name = random_user.middle_name
        phone = random_user.phone
        email = random_user.email
        password = random_user.password
        confirm_password = random_user.password
        self.click_on(registration_btn)
        self.element_is_visible(user_last_name_input).send_keys(last_name)
        self.element_is_visible(user_first_name_input).send_keys(first_name)
        self.element_is_visible(user_middle_name_input).send_keys(middle_name)
        self.element_is_visible(user_phone_input).send_keys(phone)
        self.element_is_visible(user_email_input).send_keys(email)
        self.element_is_visible(password_input).send_keys(password)
        self.element_is_visible(confirm_password_input).send_keys(confirm_password)
        self.element_is_visible(sign_up_btn).click()
        print(last_name, first_name, middle_name, phone, email, password)
        return [last_name, first_name, middle_name, phone, email, password]

    def check_authorization_module(self):
        user_data = generate_user_data()
        authorization_btn = (By.XPATH, "//li[@class='nav-item'][1]//div[@class='comments-tabs__title']")
        user_email_input = (By.CSS_SELECTOR, "input[id='loginform-identity']")
        password_input = (By.CSS_SELECTOR, "input[id='loginform-password']")
        sign_in_btn = (By.XPATH, "//div[@id='authItem1']//button[@class='btn btn-primary btn-md popup-form__btn']")
        email = user_data.email
        password = user_data.password
        self.click_on(authorization_btn)
        self.element_is_visible(user_email_input).send_keys(email)
        self.element_is_visible(password_input).send_keys(password)
        self.element_is_visible(sign_in_btn).click()
        # print(email, password)
        return [email, password]

    def check_unsuccessful_log_in_output_text(self):
        time.sleep(1)
        output_element = (By.XPATH, "//form[@id='cEnterForm']//div[@class='forms__item'][1]"
                                    "//p[@class='help-block help-block-error']")
        close_btn = (By.XPATH, "//div[@id='modalCommonAuth'][1]//button[@class='btn-close']")
        output_text = self.element_is_present(output_element).text
        self.click_on(close_btn)
        return output_text

    def close_log_in_popup(self):
        close_btn = (By.XPATH, "//div[@id='modalCommonAuth'][1]//button[@class='btn-close']")
        self.click_on(close_btn)

    def pass_add_to_compare_popup(self):
        time.sleep(0.5)
        go_to_compare_button = (By.CSS_SELECTOR, "a[class='btn btn-primary btn-md popup-form__btn']")
        compare_popup_header = (By.XPATH, "//div[@id='modalThanks']//div[@class='modal-intro-text']")
        compare_popup_text = self.element_is_present(compare_popup_header).text
        self.click_on(go_to_compare_button)
        return compare_popup_text

    def check_bucket_popup(self):
        bucket_popup_header = (By.CSS_SELECTOR, "div[class='modal-title h4']")
        bucket_popup_text = self.element_is_present(bucket_popup_header).text
        # print(bucket_popup_text)
        return bucket_popup_text

    def check_total_product_cost(self):
        addition_button = (By.CSS_SELECTOR, "button[class='product-counter__btn product-counter__btn_plus']")
        close_btn = (By.XPATH, "//div[@class='modal-content']//button[@aria-label='Close']")
        self.click_on(addition_button)
        time.sleep(1)
        product_cost = (By.CSS_SELECTOR, "div[class='thanks-page__kit-price']")
        total_cost = self.element_is_present(product_cost).text
        cost_mod = str(total_cost).replace(' ', '').replace('₴', '')
        cost = int(cost_mod)
        self.click_on(close_btn)
        print(cost)
        return cost
