from importlib.resources import path

import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def auth_file(browser, pytestconfig, tmp_path_factory):
    auth_file_path = str(tmp_path_factory.mktemp("auth") / "state.json")
    ctx = browser.new_context(base_url=pytestconfig.getoption("base_url"))
    page = ctx.new_page()
    lp = LoginPage(page)
    lp.open()
    lp.login("Admin", "admin123")
    page.wait_for_url("**/dashboard/**")
    ctx.storage_state(path=auth_file_path)
    ctx.close()
    return auth_file_path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )

@pytest.fixture(scope="function")
def browser_page(page, request):
    """
    Provides a configured Playwright page for each test.
    """

    # Standard desktop viewport
    page.set_viewport_size({
        "width": 1920,
        "height": 1080
    })

    yield page

    # Capture screenshot when test fails
    if (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    ):
        def take_screenshot(page, arg1):
            ...

        take_screenshot(    
            page,
            request.node.name
        )
    
   