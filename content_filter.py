import sys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging
logging.basicConfig(filename='/home/chatgpt/custom_utilities/utility_library/tmp/content_filter.log', level=logging.INFO)

# Get URL and keyword from command line arguments
url = sys.argv[1]
keyword = sys.argv[2]

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service('/usr/bin/chromedriver')

# Choose Chrome Browser
try:
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    logging.info('Browser launched successfully.')
except Exception as e:
    logging.error('Failed to launch browser.')
    logging.error(str(e))
    sys.exit(1)

try:
    driver.get(url)
    logging.info(f'Navigated to {url} successfully.')
except Exception as e:
    logging.error(f'Failed to navigate to {url}.')
    logging.error(str(e))
    sys.exit(1)

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Extract content
try:
    content = driver.find_elements(By.CSS_SELECTOR, "*")
    filtered_content = [el.text for el in content if keyword in el.text]
    logging.info('Content filtered successfully.')
except Exception as e:
    logging.error('Failed to filter content.')
    logging.error(str(e))
    sys.exit(1)

# Write filtered content to file
try:
    with open('/home/chatgpt/custom_utilities/utility_library/tmp/content_filter_output.txt', 'w') as f:
        for item in filtered_content:
            f.write("%s\n" % item)
    logging.info('Filtered content written to file successfully.')
except Exception as e:
    logging.error('Failed to write filtered content to file.')
    logging.error(str(e))
    sys.exit(1)

driver.quit()
logging.info('Script completed successfully.')
