import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture(scope="session")
def initialize_browser_state():
    REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    E_MAIL = "account@mail.ru"
    USERNAME = "Nikita"
    PASSWORD = "Password1"

    with sync_playwright() as paywright:
        browser = paywright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(REGISTRATION_URL)

        page.get_by_test_id("registration-form-email-input").locator("input").fill(E_MAIL)
        page.get_by_test_id("registration-form-username-input").locator("input").fill(USERNAME)
        page.get_by_test_id("registration-form-password-input").locator("input").fill(PASSWORD)

        page.get_by_test_id("registration-page-registration-button").click()
        context.storage_state(path="browser-state.json")
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page

    context.close()
    browser.close()
