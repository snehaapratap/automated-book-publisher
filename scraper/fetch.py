from playwright.sync_api import sync_playwright
import os

def fetch_text(url, output_path='data/raw/chapter1.txt'):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text('div#mw-content-text')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        browser.close()
    return content
