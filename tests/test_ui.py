from playwright.sync_api import sync_playwright
import os

def test_homepage_ui():
    os.makedirs("test_reports", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context = browser.new_context(
            ignore_https_errors=True
        )
        page = context.new_page()

        page.goto("https://example.com")

        h1 = page.locator("h1")
        assert h1.is_visible()
        assert h1.text_content() == "Example Domain"

        page.screenshot(path="test_reports/homepage.png")

        browser.close()
