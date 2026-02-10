from playwright.sync_api import expect
from pages.login_page import LoginPage
import time
import re

def test_login_valid_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    # проверяем что попали на страницу товаров
    expect(page).to_have_url(re.compile(r".*inventory.*"))


def test_login_invalid_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("nayan", "bayan")
    # проверяем что не залогинились
    expect(page).not_to_have_url(re.compile(r".*inventory.*"))
    # проверяем что появилось сообщение об ошибки
    error_message = login_page.get_error_message()
    assert ('Epic sadface: Username and password do not match any user in this service' in
            error_message), 'Некорректное сообщение о некорректной авторизации'
    time.sleep(5)
