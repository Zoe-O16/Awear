import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def initialize_driver():
    """
    Opens the web driver with Chrome
    """
    driver = webdriver.Chrome()
    return driver

# Nu alleen voor Mango, maar bouw in toekomst op vanaf de brands lijst op Zalando


def find_materials(driver, website):
    """
    Functie die navigeert van brand overview page naar brand page naar individuele items, en daar de materialen van scraped
    """

    driver.get(website)
    # Klik op brand, maar voor nu gebruik ik even 1 brand dus deze code komt later
    
    #item page
    # Wait for the accordion button to load
    wait = WebDriverWait(driver, 10)
    accordion_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//span[contains(text(), "Materiaal & wasvoorschrift")]]')
        ))

    # Click the button to expand the accordion
    accordion_button.click()

    # Wait for the expanded content to become visible
    material_content = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[@data-testid="pdp-accordion-material_care"]//dl')
        ))

    # Extract the text
    print(material_content.text)

    # Vindt materialen
    try:
        material_section = driver.find_element(By.XPATH, "//h2//button[contains(@aria-expanded, 'true')]")
        material_section.click()  # Open the material & care section
    except Exception as e:
        print("Error opening the material section:", e)
        return
    
    # Extract all material information from the page
    materials = []

    material_elements = driver.find_elements(By.XPATH, "//dl/div[contains(@class, 'qMOFyE')]")

    for element in material_elements:
        material_term = element.find_element(By.XPATH, ".//dt[contains(@role, 'term')]")
        material_value = element.find_element(By.XPATH, ".//dd[contains(@role, 'definition')]")
        
        if "Materiaal buitenlaag" in material_term.text:
            materials.append(material_value.text.strip())  # Collect material type

    
    # Print the materials and care instructions
    print("Materials Found:")
    for mat in materials:
        print(mat)

    """
    data = {
    "brand": [],
    "item_count": [],
    "avg_materials_per_item": [], analyze later
    "materials": []
    "material count": []
    """


    #xpath of regex ofzo om materiaal 1,2,3 etc te vinden
        #zorg ervoor dat ie zoveel materialen als er zijn kopieert



    #per item materials ook weer leeghalen


    #Voor kleding item een list met materials
    #in de tabel moet staan 
    #   het merk , 
    #   het aantal items wat gechecked wordt, 
    #   de hoeveelheid materialen per item gemiddeld, 
    #   alle materialen in het algemeen met een waarde per merk
    #dit moet dan geanalyseerd worden op basis van hoeveelheid items die gechecked zijn


# Main execution
if __name__ == "__main__":
    driver = initialize_driver()  # Get the driver
    website = 'https://www.zalando.nl/mango-broek-brown-m9121a3ov-o11.html' #make this dynamic later, maybe input the brand they're trying to search here
    find_materials(driver, website)  # Open the website
    driver.quit() # Close driver