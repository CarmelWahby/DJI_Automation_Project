from pages.home_page import HomePage


def test_search_icon_clickable(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_search_icon()

    assert home_page.search_input_is_visible()


def test_search_accepts_text(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_search_icon()
    home_page.enter_search_text("DJI Mini")

    assert home_page.get_search_value() == "DJI Mini"