
from playwright.sync_api import Page


class PimPage:
    def __init__(self, page: Page):
        self.page = page

        # Page headings
        self.pim_heading = page.get_by_role(
            "heading", name="PIM"
        )
        self.employee_information_heading = page.get_by_text(
            "Employee Information", exact=True
        )

        # Buttons
        self.add_button = page.get_by_role(
            "button", name="Add"
        )
        self.search_button = page.get_by_role(
            "button", name="Search"
        )
        self.reset_button = page.get_by_role(
            "button", name="Reset"
        )

        # Search fields
        self.employee_name_input = page.get_by_role(
            "textbox", name="Employee Name"
        )
        
        self.employee_id_input = self.page.locator(
            "div.oxd-input-group"
        ).filter(
        has=self.page.get_by_text("Employee Id", exact=True)
        ).locator("input")


    def open(self):
        self.page.goto(
            "/web/index.php/pim/viewEmployeeList",
            wait_until="domcontentloaded",
            timeout=600000,
        )

    def is_pim_page_visible(self) -> bool:
        """Return whether the PIM heading is visible."""
        return self.pim_heading.is_visible()

    def search_by_employee_id(self, employee_id: str):
        self.employee_id_input.fill(employee_id)
        self.search_button.click()
