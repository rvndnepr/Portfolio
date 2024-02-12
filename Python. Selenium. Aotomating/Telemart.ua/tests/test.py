# import time
from modals_and_popups.modals_and_popups import ModalsAndPopups
from pages.site_pages import MainPage
from pages.site_pages import SearchedProductPage
from pages.site_pages import CataloguePage
from pages.site_pages import CompareProductPage
from pages.site_pages import ProductPage


class TestSite:

    def test_language_popup(self, init_driver):
        main_page = MainPage(init_driver, "https://telemart.ua")
        modals_and_popups = ModalsAndPopups(init_driver)
        text_popup_lang = modals_and_popups.set_content_language_pop_up()
        text_content = main_page.choose_content_language()
        assert text_popup_lang == "Оберіть мову інтерфейсу", "There is no language_pop_up"
        assert text_content == "Покупцям", "Content text hasn't been translated"

    def test_registration_functionality(self, init_driver):
        main_page = MainPage(init_driver, "https://telemart.ua/ua")
        modals_and_popups = ModalsAndPopups(init_driver)
        main_page.go_to_user_registration()
        modals_and_popups.check_registration_module()

    def test_authorization_functionality(self, init_driver):
        main_page = MainPage(init_driver, "https://telemart.ua/ua")
        modals_and_popups = ModalsAndPopups(init_driver)
        main_page.go_to_user_registration()
        modals_and_popups.check_authorization_module()
        unsuccessful_output_text = modals_and_popups.check_unsuccessful_log_in_output_text()
        assert unsuccessful_output_text in "Невірний логін або пароль."

    def test_search_product(self, init_driver):
        main_page = MainPage(init_driver, "https://telemart.ua/ua")
        searched_product_page = SearchedProductPage(init_driver)
        catalogue_page = CataloguePage(init_driver)
        modals_and_popups = ModalsAndPopups(init_driver)
        page_product_name_text = main_page.product_type_searching()
        searched_product_text = searched_product_page.check_searched_product_page()
        catalogue_page.check_add_product_to_favourite()
        modals_and_popups.close_log_in_popup()
        assert page_product_name_text in f"Результати за пошуком «{searched_product_text}»", \
            "The page does not match the request"

    def test_choose_product_functionality(self, init_driver):
        maine_page = MainPage(init_driver, "https://telemart.ua/ua")
        catalogue_page = CataloguePage(init_driver)
        modals_and_popups = ModalsAndPopups(init_driver)
        compare_product_page = CompareProductPage(init_driver)
        product_page = ProductPage(init_driver)
        maine_page.choose_product_group_in_menu()
        catalogue_page.choose_any_product()
        text_popup_compare = modals_and_popups.pass_add_to_compare_popup()
        compare_product_page.back_to_choose_one_more_product()
        catalogue_page.choose_one_more_product()
        modals_and_popups.pass_add_to_compare_popup()
        products_count = compare_product_page.count_added_products()
        compare_icon_count = compare_product_page.check_added_products_quantity()
        product_price = compare_product_page.choose_any_product()
        product_page.check_add_product_to_bucket()
        modals_and_popups.check_bucket_popup()
        total_cost = modals_and_popups.check_total_product_cost()
        assert text_popup_compare == "Товар додан до списку порівняння", "There is no add_to_compare_popup"
        assert compare_icon_count == products_count
        # assert "Кошик" in bucket_text
        assert total_cost == 2*product_price
