from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductPage(BasePage):

    MINI_SERIES_URL = ("https://www.djistore.benda.co.il/product-category/""%d7%a8%d7%97%d7%a4%d7%a0%d7%99-%d7%a6%d7%99%d7%9c%d7%95%d7%9d/""mini-series/")

    MINI_5_PRODUCT_URL = ("https://www.djistore.benda.co.il/product/99999-955-05/")

    PRODUCT_TITLE_LINK = (By.XPATH,"//a[contains(text(),'DJI Mini 5 Pro Fly More Combo Plus')]")

    PRODUCT_PRICE = (By.CSS_SELECTOR,".jet-woo-product-price")

    ADD_TO_CART_BUTTON = (By.XPATH,"//a[contains(@aria-label,'DJI Mini 5 Pro Fly More Combo Plus')]")

    PRODUCT_TITLE = (By.XPATH,"//h1")

    PRODUCT_IMAGE = (By.XPATH,"//img[contains(@src,'MINI5PRO') or contains(@src,'Mini') or contains(@src,'mini')]")

    SKU = (By.XPATH,"//*[contains(text(),'99999-955-05')]")

    ADD_TO_CART = (By.NAME,"add-to-cart")

    def open_mini_series_page(self):
        self.open_url(self.MINI_SERIES_URL)

    def open_mini_5_product_page(self):
        self.open_url(self.MINI_5_PRODUCT_URL)

    def click_mini_5_product(self):
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PRODUCT_TITLE_LINK)
        )
        product.click()

    def is_product_title_displayed_in_category(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_TITLE_LINK)
        ).is_displayed()

    def is_product_price_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_PRICE)
        ).is_displayed()

    def is_add_to_cart_displayed(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON)).is_displayed()

    def get_product_title(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PRODUCT_TITLE)).text

    def is_product_image_displayed(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PRODUCT_IMAGE)).is_displayed()

    def get_sku(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SKU)).text

    def is_add_to_cart_displayed_on_product_page(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ADD_TO_CART)).is_displayed()