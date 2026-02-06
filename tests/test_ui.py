from playwright.sync_api import sync_playwright
import os

def test_homepage_ui():
    os.makedirs("test_reports", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://insiderone.com")

        assert page.title() != ""

        page.screenshot(path="test_reports/homepage.png")

        browser.close()
