from playwright.sync_api import Page

class DashboardPage:


    def __init__(self, page: Page):
        self.page =page


        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")

        self.user_dropdown = page.locator(".oxd-userdropdown-tab")

        self.side_menu = page.locator(".oxd-sidepanel")

    def open(self):
        """Navigate to the dashboard page."""
        self.page.goto("/web/index.php/dashboard/index")

    def is_dashboard_visible(self) -> bool:
        """Return whether the Dashboard heading is visible."""
        return self.dashboard_heading.is_visible()

    def is_user_dropdown_visible(self) -> bool:
        """Return whether the user dropdown is visible."""
        return self.user_dropdown.is_visible()

    def is_side_menu_visible(self) -> bool:
        """Return whether the side menu is visible."""
        return self.side_menu.is_visible()
    
