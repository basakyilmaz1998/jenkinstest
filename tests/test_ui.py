from playwright.sync_api import sync_playwright
import os

def test_homepage_ui():
    os.makedirs("test_reports", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://example.com")

        assert page.title() == "Example Domain"


        heading = page.locator("h1")
        assert heading.text_content() == "Example Domain"


        page.screenshot(path="test_reports/homepage.png")

        browser.close()
