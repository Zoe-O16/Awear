from selenium import webdriver


# Initialize the Chrome driver
driver = webdriver.Chrome()
website = 'https://www.zalando.nl/mango/'

# Navigate to the URL
driver.get(website)

# It's a good practice to close the browser when done
driver.quit()

