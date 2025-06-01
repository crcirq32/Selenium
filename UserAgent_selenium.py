from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent
import urllib.parse
import time
import random

#TODO
#I need more understanding of fake_useragent library

# Set up Firefox options
options = webdriver.FirefoxOptions()
options.headless = False  # Run in non-headless mode to mimic a real browser
ua = UserAgent()
user_agent = ua.random
options.set_preference("general.useragent.override", user_agent)

# Create a Service object with the path to geckodriver
service = Service(executable_path='/usr/local/bin/geckodriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)


# Define the XPath for the button #This was xpath for a button 
xpath = '/html/body/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[2]/div/div[3]/ul/li[1]/div/div/div/div[2]/div[1]/div/div/div[1]/a'

# Maximum number of attempts
max_attempts = 10

# Interval between attempts in seconds
interval = 7
# Encode the URL to handle special characters
url = '<insert_link>'
encoded_url = urllib.parse.quote(url, safe=':/')

# Print the URL to ensure it is correct
print(f"Accessing URL: {encoded_url}")

# Set a fake user agent
ua = UserAgent()
user_agent = ua.random
options.set_preference("general.useragent.override", user_agent)


# Set the User-Agent header using execute_cdp_cmd
#driver.options.set_preference('Network.setUserAgentOverride', {"userAgent": user_agent})

# Access the URL
driver.get(encoded_url)


# Loop to retry the action
# Wait until the button is present
try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
        )
    # Click the button
    button.click()
except Exception as e:
    print(f"An error occurred: {e}")
# Optionally, you can add a wait to ensure the action is completed
time.sleep(5)  # Wait for 2 seconds
