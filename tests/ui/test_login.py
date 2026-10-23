

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_page_is_displayed(page: Page):
    login_page = LoginPage(page)

    login_page.open()

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


def test_invalid_login_shows_error(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        username="invalid_user_123",
        password="wrong_password_123",
    )

    expect(login_page.login_error).to_be_visible()


def test_empty_login_shows_validation(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login_button.click()

    expect(page.get_by_text("Required", exact=True).first).to_be_visible()



def test_valid_login_opens_dashboard(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        username="Admin",
        password="admin123",
    )

    expect(login_page.dashboard_heading).to_be_visible()
    expect(page).to_have_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )