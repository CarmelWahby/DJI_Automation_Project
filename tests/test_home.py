from pages.home_page import HomePage


def test_open_dji_site(driver):

    home_page = HomePage(driver)

    home_page.open()

    assert "djistore" in driver.current_url.lower()


def test_home_page_title_not_empty(driver):

    driver.get("https://www.djistore.benda.co.il/")

    assert driver.title != ""


def test_home_page_source_not_empty(driver):

    driver.get("https://www.djistore.benda.co.il/")

    assert len(driver.page_source) > 1000