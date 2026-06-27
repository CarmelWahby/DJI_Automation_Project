import allure

@allure.title("Navigate to Mini Series page")
def test_navigate_to_mini_series_by_url(driver):
    driver.get("https://www.djistore.benda.co.il/product-category/%d7%a8%d7%97%d7%a4%d7%a0%d7%99-%d7%a6%d7%99%d7%9c%d7%95%d7%9d/mini-series/")

    assert "mini-series" in driver.current_url