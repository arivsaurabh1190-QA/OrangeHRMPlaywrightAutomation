
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

        self.login_error = page.get_by_text("Invalid credentials")
        self.dashboard_heading = page.get_by_role(
            "heading",
            name="Dashboard"
        )

    def open(self):
        self.page.goto(
            "/web/index.php/auth/login",
            wait_until="domcontentloaded",
            timeout=600000,
        )

    def login(self, username: str, password: str):
        """Enter credentials and submit the login form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_logged_in(self) -> bool:
        """Return whether the Dashboard heading is visible."""
        return self.dashboard_heading.is_visible()

    def is_login_error_visible(self) -> bool:
        """Return whether the invalid-credentials error is visible."""
        return self.login_error.is_visible()