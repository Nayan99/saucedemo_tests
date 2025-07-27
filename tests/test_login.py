from pages.login_page import LoginPage

def test_login_valid_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    # проверяем что попали на страницу товаров
    assert "inventory" in page.url


def test_login_invalid_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("nayan", "bayan")
    # проверяем что не залогинились
    assert "inventory" not in page.url
    # проверяем что появилось сообщение об ошибки
    error_message = login_page.get_error_message()
    assert error_message != ""
