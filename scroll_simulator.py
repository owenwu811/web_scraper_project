import time, sys, logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging
logging.basicConfig(filename="/home/chatgpt/custom_utilities/utility_library/tmp/scroll_simulator.log", level=logging.INFO)

url = sys.argv[1]

options = Options()
options.add_argument("--headless")

try:
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    logging.info(f"Accessed {url}")

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logging.info("Scrolled to bottom")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print(driver.page_source)
    driver.quit()
    logging.info("Script completed successfully")

except Exception as e:
    logging.error(f"An error occurred: {e}")
