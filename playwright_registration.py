from playwright.sync_api import Page, expect, sync_playwright

REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
E_MAIL = "account@mail.ru"
USERNAME = "Nikita"
PASSWORD = "Password1"


with sync_playwright() as paywright:
    browser = paywright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(REGISTRATION_URL)

    page.get_by_test_id("registration-form-email-input").locator("input").fill(E_MAIL)
    page.get_by_test_id("registration-form-username-input").locator("input").fill(USERNAME)
    page.get_by_test_id("registration-form-password-input").locator("input").fill(PASSWORD)
    page.get_by_test_id("registration-page-registration-button").click()

    title = page.get_by_test_id("dashboard-toolbar-title-text")

    expect(title).to_be_visible()
    expect(title).to_have_text("Dashboard")