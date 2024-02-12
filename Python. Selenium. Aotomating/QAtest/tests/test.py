import time
from pages.page_elements import CheckboxPage
from pages.page_elements import TextBoxPage
from pages.page_elements import RadioButtonPage
from pages.page_elements import WebTablesPage
from pages.page_elements import ButtonsPage
from pages.page_elements import LinksPage


class TestSite:

    def test_elements(self, init_driver):
        text_box_page = TextBoxPage(init_driver, "https://demoqa.com/text-box")
        # text_box_page.open_page()
        gen_user_data = text_box_page.fill_text_box_page_fields()
        full_name_text, e_mail_text, cur_address_text, perm_address_text = text_box_page.check_output_form()
        text_box_page.go_to_checkbox_page()
        assert gen_user_data.gen_name == full_name_text, "User name doesn't match"
        assert gen_user_data.gen_email == e_mail_text, "User e-mail doesn't match"
        assert gen_user_data.gen_cur_addr[:10] in cur_address_text[:10], "User current address doesn't match"
        assert gen_user_data.gen_perm_addr[:10] in perm_address_text[:10], "User permanent address doesn't match"

    def test_check_boxes(self, init_driver):
        checkbox_page = CheckboxPage(init_driver, "https://demoqa.com/checkbox")
        checkbox_page.open_full_list()
        time.sleep(0.5)
        checkbox_page.click_any_checkbox()
        checked_checkbox_items = checkbox_page.get_checked_checkboxes()
        output_list_items = checkbox_page.get_output_elements()
        print(checked_checkbox_items)
        print(output_list_items)
        checkbox_page.collapse_full_list()
        checkbox_page.go_to_radio_buttons_page()
        assert checked_checkbox_items == output_list_items

    def test_radio_buttons(self, init_driver):
        radio_buttons_page = RadioButtonPage(init_driver, "https://demoqa.com/radio-button")
        element_text = radio_buttons_page.click_any_radio_button()
        time.sleep(1)
        # output_text = radio_buttons_page.get_output_result()
        radio_buttons_page.go_to_web_tables_page()
        print(element_text)
        # print(output_text)
        # assert element_text == output_text

    # def test_radio_buttons(self, init_driver):
    #     radio_buttons_page = RadioButtonPage(init_driver, "https://demoqa.com/radio-button")
    #     radio_buttons_page.click_any_radio_button("Yes")
    #     time.sleep(0.5)
    #     output_yes = radio_buttons_page.get_output_result()
    #     radio_buttons_page.click_any_radio_button("Impressive")
    #     time.sleep(0.5)
    #     output_impressive = radio_buttons_page.get_output_result()
    #     # radio_buttons_page.click_any_radio_button("No")
    #     # output_no = radio_buttons_page.get_output_result()
    #     # radio_buttons_page.go_to_web_tables_page()
    #     assert output_yes == "Yes", "'Yes' hasn't been selected"
    #     assert output_impressive == "Impressive", "'Impressive' hasn't been selected"
    #     # assert output_no == "No", "'No' hasn't been selected"

    # def test_web_table_page(self, init_driver):
    #     web_table_page = WebTablesPage(init_driver, "https://demoqa.com/webtables")
    #     web_table_page.add_new_person()
    #     gen_person_data = web_table_page.fill_person_form()
    #     time.sleep(1)
    #     result_text = web_table_page.get_added_person_data()
    #     time.sleep(1)
    #     assert result_text[0] == gen_person_data.first_name
    #     assert result_text[1] == gen_person_data.last_name
    #     assert result_text[2] == gen_person_data.age
    #     assert result_text[3] == gen_person_data.e_mail
    #     assert result_text[4] == gen_person_data.salary
    #     assert result_text[5] in gen_person_data.department

    def test_web_table_page(self, init_driver):
        web_table_page = WebTablesPage(init_driver, "https://demoqa.com/webtables")
        web_table_page.add_new_person()
        gen_person_data = web_table_page.fill_person_form()
        time.sleep(1)
        result_text = web_table_page.get_added_person_data()
        time.sleep(1)
        # print(gen_person_data)
        # print(result_text)
        assert gen_person_data in result_text

    def test_web_table_search_person(self, init_driver):
        web_table_page = WebTablesPage(init_driver, "https://demoqa.com/webtables")
        web_table_page.add_new_person()
        e_mail = web_table_page.fill_person_form()[3]
        web_table_page.search_person(e_mail)
        table_result = web_table_page.check_search_person()
        # print(e_mail)
        # print(table_result)
        assert e_mail in table_result, "The person wasn't found"

    def test_web_table_update_person_info(self, init_driver):
        web_table_page = WebTablesPage(init_driver, "https://demoqa.com/webtables")
        web_table_page.add_new_person()
        e_mail = web_table_page.fill_person_form()[3]
        web_table_page.search_person(e_mail)   # Searching by the mostly unique value
        salary = web_table_page.update_person_info()
        updated_data_row = web_table_page.check_search_person()
        # print(salary)
        # print(updated_data_row)
        assert salary in updated_data_row, "Person's data were not changed"

    def test_web_table_delete_person(self, init_driver):
        web_table_page = WebTablesPage(init_driver, "https://demoqa.com/webtables")
        web_table_page.add_new_person()
        e_mail = web_table_page.fill_person_form()[3]
        web_table_page.search_person(e_mail)
        web_table_page.delete_added_person()
        no_rows_text = web_table_page.check_person_deleted()
        assert no_rows_text == "No rows found"

    def test_web_table_add_rows(self, init_driver):
        web_table_page = WebTablesPage(init_driver, "https://demoqa.com/webtables")
        checked_rows = web_table_page.change_rows_count()
        actual_rows = web_table_page.check_rows_count()
        web_table_page.go_to_buttons_page()
        time.sleep(1)
        print(checked_rows)
        print(actual_rows)
        assert checked_rows == actual_rows

    def test_buttons_clicks(self, init_driver):
        buttons_page = ButtonsPage(init_driver, "https://demoqa.com/buttons")
        double_button_text = buttons_page.click_on_double_click_buttons()
        time.sleep(0.5)
        right_button_click_text = buttons_page.click_on_right_click_buttons()
        time.sleep(0.5)
        simple_click_text = buttons_page.click_on_simple_click_buttons()
        time.sleep(0.5)
        buttons_page.go_to_links_page()
        assert double_button_text == "You have done a double click",  "The double click button was not clicked"
        assert right_button_click_text == "You have done a right click", "The right click button was not clicked"
        assert simple_click_text == "You have done a dynamic click",  "The dynamic click button was not clicked"

    def test_normal_links(self, init_driver):
        links_page = LinksPage(init_driver, "https://demoqa.com/links")
        href_link, current_url = links_page.check_working_link()
        assert href_link == current_url, "the link is broken or url is incorrect"

    def test_broken_links(self, init_driver):
        links_page = LinksPage(init_driver, "https://demoqa.com/links")
        result = links_page.check_broken_link('https://demoqa.com/bad-request')
        links_page.go_to_broken_links_page()
        assert result == 400, "the link works or the status code in son 400"
