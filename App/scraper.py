import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re



def wait():
    # globale wait functie maken

    return None
def initialize_driver():
    """
    Opens the web driver with Chrome
    """
    driver = webdriver.Chrome()
    return driver

def handle_popups(driver):
    """
    Handles  popups: cookie consent banner
    """
    try:
        # Wait for the cookie consent popup
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "usercentrics-root"))
        )
        print("Cookie consent popup detected.")
        
        # Close the "Deny All" button if present - hier gaat het mis!!
        deny_all_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='uc-deny-all-button']"))
        )
        deny_all_button.click()
        print("Deny All button clicked.")

    except Exception as e:
        print("Error handling popups:", e)

def find_materials(driver, website):
    """
    Functie die navigeert van brand overview page naar brand page naar individuele items, en daar de materialen van scraped
    """

    driver.get(website)
    # Navigate to brand page: for now I'll be using 1 brand to develop the rest
    handle_popups(driver)
    # Navigate to item page

    # Item page
    #   Open materials section on page
    #   Wait until things are clickable
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h2//button[contains(@aria-expanded, 'false')]"))
        )
        material_section = driver.find_element(By.XPATH, "//h2//button[contains(@aria-expanded, 'false')]")
        material_section.click()  # Open the material & care section
        print("Material section found:", material_section)
    except Exception as e:
        print("Error opening the material section:", e)
        return
    
    # Extract all material information
    materials = []

    material_elements = driver.find_elements(By.XPATH, "//dl/div[contains(@class, 'qMOFyE')]")
    print("Material elements found:", len(material_elements))


    
    
        # Iterate over material values
        # Finds material terms and values
        #   Terms indicate things like "materiaal buitenlaag" and "voering"
        #   Values indicate the fabric type
    for element in material_elements:
        try:
            material_term = material_elements.find_element(By.XPATH, ".//dt[contains(@role, 'term')]")
            material_value = material_elements.find_element(By.XPATH, ".//dd[contains(@role, 'definition')]")

            # Get the string
            material_string = material_value.text.strip().lower()
            print(f"Material string found: {material_string}")
            # If the material string contains multiple materials
            if ',' in material_string:
                # Split the string into individual materials by the comma
                materials_list = [mat.strip() for mat in material_string.split(',')]
                for mat in materials_list:
                    # Remove percentages using regex
                    material_name = re.sub(r'\d+%', '', mat).strip()
                    materials.append(material_name)
            # In case of one material
            else:
                # Remove percentages using regex
                material_name = re.sub(r'\d+%', '', material_string).strip()
                materials.append(material_name)

        except Exception as e:
            print("Error extracting materials:", e)
    
    # Print the materials
        #xpath of regex ofzo om materiaal 1,2,3 etc te vinden
        #zorg ervoor dat ie zoveel materialen als er zijn kopieert
    if materials:
        print("Materials Found:")
        for mat in materials:
            print(mat)
    else:
        print("No materials found.")
    
    #per item materials ook weer leeghalen


    #Voor kleding item een list met materials
    #in de tabel moet staan 
    #   het merk , 
    #   het aantal items wat gechecked wordt, 
    #   de hoeveelheid materialen per item gemiddeld, 
    #   alle materialen in het algemeen met een waarde per merk
    #dit moet dan geanalyseerd worden op basis van hoeveelheid items die gechecked zijn
    #dit stopt ie in een dataframe
    """
    data = {
    "brand": [],
    "item_count": [],
    "avg_materials_per_item": [], analyze later
    "materials": []
    "material count": []
    """

def brand_data(driver):
    """saves data to database"""

# Main execution
if __name__ == "__main__":
    driver = initialize_driver()  # Get the driver
    # Nu alleen voor Mango, maar bouw in toekomst op vanaf de brands lijst op Zalando
    website = 'https://www.zalando.nl/mango-broek-brown-m9121a3ov-o11.html' #make this dynamic later, maybe input the brand they're trying to search here
    find_materials(driver, website)  # Open the website



#notes
#     Possible path: //div[@data-testid="pdp-accordion-material_care"]//dl'
