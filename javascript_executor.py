import sys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging
logging.basicConfig(filename='/home/chatgpt/custom_utilities/utility_library/tmp/javascript_executor.log', level=logging.INFO)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service('/usr/bin/chromedriver')

# Get URL and JavaScript command from command line arguments
url = sys.argv[1]
js_command = sys.argv[2]

logging.info(f"Starting JavaScript executor for URL: {url} with command: {js_command}")

try:
    # Initialize webdriver
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    logging.info("Navigating to URL...")
    # Open URL
    driver.get(url)

    logging.info("Executing JavaScript command...")
    # Execute JavaScript command
    result = driver.execute_script(js_command)

    logging.info(f"JavaScript command executed. Result: {result}")

    driver.quit()
    logging.info("Script completed.")

except Exception as e:
    logging.error(f"Error occurred: {e}")
