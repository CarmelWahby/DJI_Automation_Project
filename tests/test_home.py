import allure
from pages.home_page import HomePage


@allure.title("Open DJI Store website")
def test_open_dji_site(driver):

    home_page = HomePage(driver)

    home_page.open()

    assert "djistore" in driver.current_url.lower()


@allure.title("Verify home page title")
def test_home_page_title_not_empty(driver):

    driver.get("https://www.djistore.benda.co.il/")

    assert driver.title != ""


@allure.title("Verify home page source is not empty")
def test_home_page_source_not_empty(driver):

    driver.get("https://www.djistore.benda.co.il/")

    assert "djistore" in driver.current_url.lower()