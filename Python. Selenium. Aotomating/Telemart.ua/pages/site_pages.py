import time
from random import randint
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def choose_content_language(self):
        for_customers_dropdown = (By.XPATH, "//li[@class='header-navi__item'][1]//div[@class='dropdown-box__header']")
        customers_dropdown_text = self.element_is_present(for_customers_dropdown).text
        return customers_dropdown_text

    def go_to_user_registration(self):
        user_profile_btn = (By.XPATH, "//div[@class='header-center']//button[@class='btn btn_user']")
        self.element_is_visible(user_profile_btn).click()

    def product_type_searching(self):
        product_list = ["Комп'ютер", "Процесор", "Монітор", "Корпус", "ОЗП", "Відеокарта", "Блок живлення",
                        "Клавіатура", "Ноутбук", "Навушники"]
        random_product = randint(0, len(product_list) - 1)
        search_field = (By.CSS_SELECTOR, "input[name='search_que']")
        search_button = (By.CSS_SELECTOR, "button[class='btn btn_secondary search__btn']")
        self.element_is_visible(search_field).send_keys({product_list[random_product]})
        self.click_on(search_button)
        print(product_list[random_product])
        return product_list[random_product]

    def choose_product_group_in_menu(self):
        time.sleep(0.5)
        catalogue_button = (By.CSS_SELECTOR, "div[class='btn btn_primary catalog-box__btn']")
        product_group_line = (By.XPATH, f"//div[@class='nav catalog-box__navi']//button[@type='button']"
                                        f"[{randint(1, 5)}]")
        product_type_button = (By.XPATH, "//div[@class='tab-pane fade active show']"
                                         "//div[@class='catalog-box__item-title'][1]")
        self.click_on(catalogue_button)
        group_line = self.element_is_visible(product_group_line)
        self.move_to_element(group_line)
        self.element_is_present(product_group_line).click()
        try:
            self.element_is_present(product_type_button).click()
        except:
            self.driver.back()
            group_line = self.element_is_visible(product_group_line)
            self.move_to_element(group_line)
            self.element_is_present(product_group_line).click()
            self.element_is_present(product_type_button).click()


class SearchedProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_searched_product_page(self):
        product_type_page_element = (By.CSS_SELECTOR, "div[class='page-main-header']")
        searched_product_type_page = self.element_is_present(product_type_page_element).text
        return searched_product_type_page.splitlines()


class CataloguePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_add_product_to_favourite(self):
        favour_btn = (By.XPATH, f"//div[@data-prod-position='{randint(1, 24)}']"
                                f"//button[@class='btn btn_ghost preview-product__btn preview-product__btn_favorite']")
        add_to_favour_btn = self.element_is_visible(favour_btn)
        self.move_to_element(add_to_favour_btn)
        time.sleep(1)
        self.click_on(favour_btn)

    def choose_any_product(self):
        time.sleep(1)
        # product_position = randint(1, 24)
        any_product_compare_button = (By.XPATH, f"//div[@data-prod-position='{randint(1, 24)}']"
                                                f"//button[@type='button'][1]")
        product_name = (By.XPATH, f"//div[@data-prod-position='{randint(1, 24)}']//div[@class='product-item__title']")
        product_name_text = self.element_is_present(product_name).text
        compare_button = self.element_is_visible(any_product_compare_button)
        self.move_to_element(compare_button)
        time.sleep(1)
        self.click_on(any_product_compare_button)
        print(product_name_text)
        return product_name_text

    def choose_one_more_product(self):
        time.sleep(1)
        # product_position = randint(1, 24)
        one_more_product_compare_button = (By.XPATH, f"//div[@data-prod-position='{randint(1, 24)}']"
                                                     f"//button[@type='button'][1]")
        product_name = (By.XPATH, f"//div[@data-prod-position='{randint(1, 24)}']//div[@class='product-item__title']")
        product_name_text = self.element_is_present(product_name).text
        compare_button = self.element_is_visible(one_more_product_compare_button)
        self.move_to_element(compare_button)
        time.sleep(1)
        self.click_on(one_more_product_compare_button)
        print(product_name_text)
        return product_name_text


class CompareProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def back_to_choose_one_more_product(self):
        self.driver.back()

    def count_added_products(self):
        products = (By.CSS_SELECTOR, "div[class='preview-product preview-product_column product_wrapper']")
        product_list = self.elements_are_visible(products)
        result = []
        for item in product_list:
            result.append(item)
        product_count = len(result)
        return product_count

    def check_added_products_quantity(self):
        products_quantity_icon = (By.CSS_SELECTOR, "span[class='header__quan']")
        icon_text = self.element_is_present(products_quantity_icon).text
        icon = int(icon_text)
        return icon

    def choose_any_product(self):
        time.sleep(1)
        added_products = (By.CSS_SELECTOR, "div[class='preview-product preview-product_column product_wrapper']")
        product_list = self.elements_are_visible(added_products)
        result = []
        for item in product_list:
            result.append(item)
        product_number = randint(1, len(result))
        chosen_product = (By.XPATH, f"//div[@data-prod-position='{product_number}']")
        random_product_price = (By.XPATH, f"//div[@data-prod-position='{product_number}']//div[@class='product-cost']")
        time.sleep(1)
        product_price = self.element_is_present(random_product_price).text
        price_mod = str(product_price).replace(' ', '').replace('₴', '')
        price = int(price_mod)
        self.click_on(chosen_product)
        print(price)
        return price

        # self.click_on(any_added_product)
        # first_added_product_price = (By.XPATH, "//div[@data-prod-position='1']//div[@class='product-cost']")
        # second_added_product_price = (By.XPATH, "//div[@data-prod-position='2']//div[@class='product-cost']")
        # first_added_product = (By.XPATH, "//div[@data-prod-position='1']")
        # second_added_product = (By.XPATH, "//div[@data-prod-position='2']")
        # first_added_product_name = (By.XPATH, "//div[@data-prod-position='1']//a[@class='preview-product__title']")
        # second_added_product_name = (By.XPATH, "//div[@data-prod-position='2']//a[@class='preview-product__title']")
        # first_product_price = self.element_is_present(first_added_product_price).text
        # second_product_price = self.element_is_present(second_added_product_price).text
        # first_price = str(first_product_price).replace(' ', '').replace('₴', '')
        # second_price = str(second_product_price).replace(' ', '').replace('₴', '')
        # price_1 = int(first_price)
        # price_2 = int(second_price)
        # print(price_1)
        # print(price_2)
        # first_product_name_text = self.element_is_present(first_added_product_name).text
        # second_product_name_text = self.element_is_present(second_added_product_name).text
        # if price_1 <= price_2:
        #     self.click_on(first_added_product)
        #     print(first_product_name_text)
        #     return first_product_name_text
        # else:
        #     self.click_on(second_added_product)
        #     print(second_product_name_text)
        #     return second_product_name_text


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_add_product_to_bucket(self):
        buy_btn = (By.CSS_SELECTOR, "a[class='btn btn_primary btn-lg card-block__price-btn add-to-cart']")
        self.click_on(buy_btn)
