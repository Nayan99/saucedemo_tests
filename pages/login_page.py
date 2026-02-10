from playwright.sync_api import Page, expect
import test_data as td

class LoginPage:
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = '.error-message-container'

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto(td.BASE_URL, wait_until='domcontentloaded')

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
        self.page.wait_for_load_state('domcontentloaded')

    def get_error_message(self) -> str:
        error = self.page.locator(self.ERROR_MESSAGE)
        expect(error).to_be_visible()
        return error.inner_text().strip()
