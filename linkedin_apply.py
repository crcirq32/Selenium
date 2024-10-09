from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Path to Geckodriver
geckodriver_path = "/usr/local/bin/geckodriver"  # Update this if necessary

# Create a Service object for the Firefox driver
service = Service(executable_path=geckodriver_path)

# Initialize the Firefox driver with the service
driver = webdriver.Firefox(service=service)


# Allow the page to load
time.sleep(3)

# Log in to LinkedIn
# Open linkedin page
driver.get('https://www.linkedin.com/login')
email = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
email.send_keys('<insert_UN')
password.send_keys('<insert_PW>')
password.send_keys(Keys.RETURN)

# Wait until logged in
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'global-nav-typeahead'))
)

# Go to the jobs page
driver.get('https://www.linkedin.com/jobs/')

# Search for jobs
search_box = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
search_box.send_keys('Remote')  # Replace 'Remote' with desired job title
search_box.send_keys(Keys.RETURN)

# Wait until search results are loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'job-card-container'))
)
# Loop through job listings and apply
jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')
for job in jobs:
    try:
        # Click the job to open the details
        job.click()
        time.sleep(2)  # Wait for the page to load

        # Click the Easy Apply button
        easy_apply_button = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")
        easy_apply_button.click()
        time.sleep(2)

    except Exception as e:
        print(f"Could not apply for job: {e}")
        continue
        
#TODO: 
#Create a while loop that will recursively click "next" button
#next_button = driver.find_element(By.XPATH, "//button[contains(@class, 'Next')]")
#Create a action to "submit-application"
#easy_apply_button = driver.find_element(By.XPATH, "//button[contains(@class, 'Submit application')]")
