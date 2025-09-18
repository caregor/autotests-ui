from playwright.sync_api import Page, expect, sync_playwright

REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
E_MAIL = "account@mail.ru"
USERNAME = "Nikita"
PASSWORD = "Password1"


with sync_playwright() as paywright:
    browser = paywright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(REGISTRATION_URL)

    registration_button = page.get_by_test_id("registration-page-registration-button")

    page.get_by_test_id("registration-form-email-input").locator("input").fill(E_MAIL)
    page.get_by_test_id("registration-form-username-input").locator("input").fill(USERNAME)
    page.get_by_test_id("registration-form-password-input").locator("input").fill(PASSWORD)

    page.get_by_test_id("registration-page-registration-button").click()
    context.storage_state(path="browser-state.json")

    new_session = browser.new_context(storage_state="browser-state.json")
    page = new_session.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(title).to_be_visible()
    expect(title).to_have_text("Courses")

    icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(text).to_be_visible()
    expect(text).to_have_text("There is no results")

    description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(description).to_be_visible()
    expect(description).to_have_text("Results from the load test pipeline will be displayed here")


