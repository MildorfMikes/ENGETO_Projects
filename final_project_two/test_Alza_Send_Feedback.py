# Test #3 Milan Mike Klos

# find Kontakt - ostatní - nahlášení chyby / návrh na zlepšení - Internetový obchod - vyplnit dotazník - zavřít
    # close cookies and assistant

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    
    page = context.new_page()

    # Open Alza.cz
    page.goto("https://www.alza.cz/")

    # Click on cookies
    page.get_by_role("link", name="Rozumím").click()
    
    # Select Kontakty
    page.goto("https://www.alza.cz/contact")
    
    # Close assistent
    page.get_by_role("button", name="Ukončit a zavřít").click()
    
    # Select category Ostatní
    page.get_by_test_id("contact-navigation-other").click()

    # Close cookies again
    page.get_by_role("link", name="Rozumím").click()
    
    # Select Nahlášení chyb
    page.get_by_role("link", name="Nahlášení chyby / návrh na").click()
    
    # Select subcategory
    page.get_by_role("link", name="Internetový obchod").click()
    
    # Click in text input field
    page.get_by_test_id("question-text").get_by_role("textbox").click()
    
    # Wait for a second
    page.wait_for_timeout(1000)
    
    # Fill in text input field
    page.get_by_test_id("question-text").get_by_role("textbox").fill("nemusi porad skakat asistentka Alzee")
    
    # Wait for a second
    page.wait_for_timeout(1000)
    
    # Close assistant again
    page.get_by_role("button", name="Ukončit a zavřít").click()

    # Wait for a second
    page.wait_for_timeout(1000)
    
    # Click on Name input field
    page.get_by_test_id("question-fullname").get_by_role("textbox").click()
    
    # Wait for a second
    page.wait_for_timeout(1000)
    
    # Fil in Name
    page.get_by_test_id("question-fullname").get_by_role("textbox").fill("Pepa Pepíků")

    # Wait for a second  
    page.wait_for_timeout(1000)
    
    # Click on email input field
    page.get_by_test_id("question-email").get_by_role("textbox").click()
    
    # Wait for a second
    page.wait_for_timeout(1000)
    
    # Fill in email
    page.get_by_test_id("question-email").get_by_role("textbox").fill("@ne")
    
    # Wait for a second
    page.wait_for_timeout(1000)

    # Exit
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



   
   
   
   
   
   
   
   
   
  