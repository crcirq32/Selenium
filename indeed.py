from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time

# Path to the ChromeDriver (you can replace this with the path to your driver)
driver_path = "/usr/local/bin/geckodriver"  # Update with your own path

#object to store driver path in "service"
service = Service(driver_path)

#open driver instance with firefox
driver = webdriver.Firefox(service=service)

# Open Indeed
driver.get("https://www.indeed.com")

# Allow the page to load
time.sleep(2)

# Find the search input for job titles/keywords
search_box = driver.find_element("xpath", '//*[@id="text-input-what"]')
search_box.clear()
search_box.send_keys("data entry")  # Replace with any job title

# Find the location input and set it to "Remote"
location_box = driver.find_element("xpath", '//*[@id="text-input-where"]')
location_box.clear()  # Clear the default location
location_box.send_keys("Remote")

# Press Enter to search
search_box.send_keys(Keys.RETURN)

# Allow the search results to load
time.sleep(3)

# (Optional) Scroll down to load more results
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Print the job titles from the results (as an example)
job_titles = driver.find_elements("xpath", '//h2[@class="jobTitle"]')
for index, title in enumerate(job_titles[:10]):  # Print top 10 results
    print(f"Job {index + 1}: {title.text}")

# Close the browser
#driver.quit()

