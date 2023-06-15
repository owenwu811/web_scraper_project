import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Setup WebDriver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL to execute JS
url = sys.argv[1]

# Navigate to URL
driver.get(url)

# Wait for JS to load
time.sleep(5)

# Execute JS
result = driver.execute_script("return document.documentElement.outerHTML")

# Save result to file
with open("/home/chatgpt/custom_utilities/utility_library/tmp/javascript_executor_output.txt", "w") as file:
    file.write(result)

# Close WebDriver
driver.quit()
