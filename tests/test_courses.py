import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

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
