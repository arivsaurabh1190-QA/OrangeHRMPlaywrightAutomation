
from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.pim_page import PimPage


def test_pim_page_displays_employee_information(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    pim_page = PimPage(page)

    # Step 1: Open the login page
    login_page.open()

    # Step 2: Log in
    login_page.login(
        username="Admin",
        password="admin123",
    )

    # Step 3: Verify that login succeeded
    expect(dashboard_page.dashboard_heading).to_be_visible()

    # Step 4: Navigate to the PIM employee list
    pim_page.open()

    # Step 5: Verify the PIM page elements
    expect(pim_page.pim_heading).to_be_visible()
    expect(pim_page.employee_information_heading).to_be_visible()
    expect(pim_page.add_button).to_be_visible()
    expect(pim_page.search_button).to_be_visible()
    expect(pim_page.reset_button).to_be_visible()


def test_search_employee_by_id(page: Page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)

    # Log in
    login_page.open()
    login_page.login(
        username="Admin",
        password="admin123",
    )

    expect(login_page.dashboard_heading).to_be_visible()

    # Open PIM
    pim_page.open()

    # Search for Amelia using Employee ID
    pim_page.search_by_employee_id("01715")

    # Verify the matching employee appears
    employee_row = page.get_by_role("row").filter(has_text="01715")
    expect(employee_row).to_contain_text("Amelia")
    expect(employee_row).to_contain_text("Brown")
