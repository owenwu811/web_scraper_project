from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging

# Set up logging
logging.basicConfig(filename='/home/chatgpt/custom_utilities/utility_library/tmp/site_mapper.log', level=logging.INFO)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service('/usr/bin/chromedriver')

# Start a new browser session
logging.info("Starting a new browser session...")
try:
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
except Exception as e:
    logging.error(f"Error occurred: {e}")
    exit(1)

# Navigate to the webpage
logging.info("Navigating to the webpage...")
try:
    driver.get("https://www.example.com") # replace with your website
except Exception as e:
    logging.error(f"Error occurred: {e}")
    exit(1)

# Get all links on the page
logging.info("Getting all links on the page...")
try:
    links = driver.find_elements(By.TAG_NAME, "a")
except Exception as e:
    logging.error(f"Error occurred: {e}")
    exit(1)

# Open the output file
with open("/home/chatgpt/custom_utilities/utility_library/tmp/sitemap.txt", "w") as f:
    # Write all links to the file
    logging.info("Writing all links to the file...")
    for link in links:
        try:
            f.write(link.get_attribute("href") + "\n")
        except Exception as e:
            logging.error(f"Error occurred: {e}")

# Close the browser session
logging.info("Closing the browser session...")
driver.quit()
