from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to Geckodriver
geckodriver_path = "/usr/local/bin/geckodriver"  # Update this if necessary

# Create a Service object for the Firefox driver
service = Service(executable_path=geckodriver_path)

# Initialize the Firefox driver with the service
driver = webdriver.Firefox(service=service)

# Open DuckDuckGo search page
driver.get("https://www.duckduckgo.com")

# Allow the page to load
time.sleep(2)

# Find the search box element by its name attribute
search_box = driver.find_element("name", "q")

# Type 'cat images' into the search box
search_box.send_keys("cat images")

# Press Enter to initiate the search
search_box.send_keys(Keys.RETURN)

# Allow results to load
time.sleep(3)

# Find and click on the 'Images' tab to filter results to images
images_tab = driver.find_element("link text", "Images")
images_tab.click()

# Allow images to load
time.sleep(3)

# Print the title of the current page (just to verify the search worked)
print(driver.title)

# Optionally, you could print some image links or perform further actions here.
# For example, getting the first few image links (if desired):
image_elements = driver.find_elements("css selector", "img.tile--img__img")
for index, img in enumerate(image_elements[:5]):  # Print top 5 images
    print(f"Image {index + 1}: {img.get_attribute('src')}")

# Close the browser
driver.quit()
