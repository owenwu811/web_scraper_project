from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver
webdriver_service = Service("/usr/bin/chromedriver")

# Initialize webdriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open URL
driver.get(sys.argv[1])

# Print the title of the page
title = driver.title
print(f"Title of the page is: {title}")

driver.quit()
