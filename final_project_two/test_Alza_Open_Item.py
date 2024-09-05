# Test #1 Milan Mike Klos

# open Alza - find iPhone - select first result - open - close

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Run the browser in a visible mode
    page = browser.new_page()

    # Visit the Alza homepage
    page.goto("https://www.alza.cz/")

    # Wait for 1 second
    page.wait_for_timeout(1000)

    # Close the cookie consent if it appears
    # We wait for the "Rozumím" button (or similar) to be visible and click it
    if page.locator(".js-cookies-info-accept").is_visible():
        page.locator(".js-cookies-info-accept").click()

    # Wait for 1 second
    page.wait_for_timeout(1000)

    # Search for a product (e.g., "iPhone")
    page.fill('input[placeholder="Co hledáte? Např. kabel AlzaPower..."]', "iPhone")

    # Wait for 1 second
    page.wait_for_timeout(1000)

    # Press the Enter key to start the search
    page.keyboard.press("Enter")

    # Wait for the search results to load
    page.wait_for_selector(".browsingitem")

    # Wait for 1 second before clicking the product
    page.wait_for_timeout(1000)

    # Click on the first product in the results
    page.locator(".browsingitem").first.click()

    # Wait for 1 second before closing the browser
    page.wait_for_timeout(1000)

    # Close the browser after completing the actions
    browser.close()
