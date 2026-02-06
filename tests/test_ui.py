from playwright.sync_api import Page

def test_homepage(page: Page):
    page.goto("https://insiderone.com")

    page.screenshot(path="test_reports/homepage.png")

    assert "Insider" in page.title()
