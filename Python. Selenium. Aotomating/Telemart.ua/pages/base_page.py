from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def move_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on(self, locator, timeout=5):
        Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator)).click()

    def send_keys_to(self, locator, text, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator, timeout=5):
        element = Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        return element.text

    def clear_in(self, locator, timeout=5):
        Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator)).clear()
