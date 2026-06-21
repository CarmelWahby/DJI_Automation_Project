import allure
from pages.home_page import HomePage


@allure.title("Verify search popup opens")
def test_search_icon_clickable(driver):
    home_page = HomePage(driver)

    with allure.step("Open homepage"):
        home_page.open()

    with allure.step("Click search icon"):
        home_page.click_search_icon()

    with allure.step("Verify search input is visible"):
        assert home_page.search_input_is_visible()


@allure.title("Verify search field accepts text")
def test_search_accepts_text(driver):
    home_page = HomePage(driver)

    with allure.step("Open homepage"):
        home_page.open()

    with allure.step("Click search icon"):
        home_page.click_search_icon()

    with allure.step("Enter search text"):
        home_page.enter_search_text("DJI Mini")

    with allure.step("Verify search text was entered"):
        assert home_page.get_search_value() == "DJI Mini"