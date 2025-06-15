from playwright.sync_api import sync_playwright
import os

def take_screenshot(url, path='data/screenshots/chapter1.png'):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page.screenshot(path=path)
        browser.close()
