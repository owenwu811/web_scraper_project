import os, sys, time, logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

# Setup logging
logging.basicConfig(filename='/home/chatgpt/custom_utilities/utility_library/tmp/employment_projections_scraper.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setup WebDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Define function to check if element exists
def check_exists_by_xpath(xpath):
    try:
        wd.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# Navigate to the webpage
logging.info('Navigating to the webpage...')
wd.get('https://www.bls.gov/lpc/data.htm')

# Wait for the page to load
logging.info('Waiting for the page to load...')
time.sleep(5)

# Find the links to the tables
logging.info('Finding the links to the tables...')
links = wd.find_elements(By.XPATH, '//a[contains(@href, .xlsx)]')

# Download the XLSX files
for link in links:
    url = link.get_attribute('href')
    logging.info(f'Downloading file from {url}...')
    os.system(f'wget -P /home/chatgpt/custom_utilities/utility_library/tmp/ {url}')

# Close the WebDriver
wd.quit()
logging.info('Web scraping completed.')
