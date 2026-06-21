import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://www.djistore.benda.co.il/"

    SEARCH_ICON = (By.XPATH,"//a[contains(@href,'popup') or contains(@href,'elementor-action')]")

    SEARCH_INPUTS = (By.XPATH,"//input[@type='search' or contains(@placeholder,'חפש מוצר')]")

    def open(self):
        self.open_url(self.URL)

    def click_search_icon(self):
        icons = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.SEARCH_ICON))

        self.driver.execute_script("arguments[0].scrollIntoView(true);",icons[0])

        self.driver.execute_script("arguments[0].click();",icons[0])

        time.sleep(2)

    def get_visible_search_input(self):
        inputs = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.SEARCH_INPUTS))

        for input_element in inputs:
            if input_element.is_displayed() and input_element.is_enabled():
                return input_element

        raise Exception("No visible search input found")

    def search_input_is_visible(self):
        return self.get_visible_search_input().is_displayed()

    def enter_search_text(self, text):
        search_input = self.get_visible_search_input()
        search_input.click()
        search_input.clear()
        search_input.send_keys(text)

    def get_search_value(self):
        return self.get_visible_search_input().get_attribute("value")