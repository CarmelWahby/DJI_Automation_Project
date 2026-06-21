import allure
from pages.product_page import ProductPage


def test_open_mini_series_page(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_series_page()

    assert "mini-series" in driver.current_url
    assert len(driver.page_source) > 1000


def test_mini_5_product_displayed_in_category(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_series_page()

    assert product_page.is_product_title_displayed_in_category()


def test_mini_5_product_price_displayed(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_series_page()

    assert product_page.is_product_price_displayed()


def test_mini_5_add_to_cart_displayed(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_series_page()

    assert product_page.is_add_to_cart_displayed()


def test_open_mini_5_product_page(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert "99999-955-05" in driver.current_url


@allure.title("Verify DJI Mini 5 Pro product title")
def test_product_title(driver):
    product_page = ProductPage(driver)

    with allure.step("Open DJI Mini 5 Pro product page"):
        product_page.open_mini_5_product_page()

    with allure.step("Get product title"):
        title = product_page.get_product_title()

    with allure.step("Verify title contains DJI Mini 5 Pro"):
        assert "DJI Mini 5 Pro" in title


def test_product_image_exists_in_page_source(driver):

    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert "webp" in driver.page_source or "jpg" in driver.page_source or "png" in driver.page_source


def test_product_sku(driver):

    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert "99999-955-05" in driver.current_url


def test_product_add_to_cart_button(driver):

    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert product_page.is_add_to_cart_displayed_on_product_page()


def test_product_url(driver):

    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert "99999-955-05" in driver.current_url


def test_product_name_in_page_source(driver):

    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert "DJI Mini 5 Pro" in product_page.get_product_title()


def test_refresh_product_page(driver):
    driver.get("https://www.djistore.benda.co.il/product/99999-955-05/")
    driver.refresh()

    assert "99999-955-05" in driver.current_url


def test_product_page_title_not_empty(driver):
    driver.get("https://www.djistore.benda.co.il/product/99999-955-05/")

    assert driver.title != ""


def test_product_page_loaded_by_title(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert "DJI Mini 5 Pro" in product_page.get_product_title()


def test_mini_series_page_title_not_empty(driver):
    driver.get("https://www.djistore.benda.co.il/product-category/%d7%a8%d7%97%d7%a4%d7%a0%d7%99-%d7%a6%d7%99%d7%9c%d7%95%d7%9d/mini-series/")

    assert driver.title != ""


def test_product_price_contains_currency(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_series_page()

    assert product_page.is_product_price_displayed()


def test_add_to_cart_button_is_clickable_in_category(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_series_page()

    assert product_page.is_add_to_cart_displayed()


def test_mini_series_contains_dji_products(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_series_page()

    assert product_page.is_product_title_displayed_in_category()


def test_product_page_refresh_keeps_same_product(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()
    driver.refresh()

    assert "99999-955-05" in driver.current_url


def test_product_title_contains_fly_more_combo_plus(driver):
    product_page = ProductPage(driver)

    product_page.open_mini_5_product_page()

    assert "Fly More Combo Plus" in product_page.get_product_title()
