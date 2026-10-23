from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_dashboard_opens_after_login(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.open()
    login_page.login(
        username="Admin",
        password="admin123",
    )

    expect(dashboard_page.dashboard_heading).to_be_visible()
    expect(dashboard_page.user_dropdown).to_be_visible()
    expect(dashboard_page.side_menu).to_be_visible()