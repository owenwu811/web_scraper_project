import sys, logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Set up logging
logging.basicConfig(filename='/home/chatgpt/custom_utilities/utility_library/tmp/login_manager.log', level=logging.ERROR)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service('/usr/bin/chromedriver')

try:
    # Initialize webdriver
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    logging.info("Webdriver initialized.")

    # Open URL
    driver.get(sys.argv[1])
    logging.info(f"Navigated to {sys.argv[1]}.")

    # Wait for the username field to be clickable
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    logging.info("Username field is clickable.")

    # Type username into the username field
    username_field.send_keys(sys.argv[2])
    logging.info("Username entered.")

    # Wait for the password field to be clickable
    password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    logging.info("Password field is clickable.")

    # Type password into the password field
    password_field.send_keys(sys.argv[3])
    logging.info("Password entered.")

    # Wait for the login button to be clickable
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
    logging.info("Login button is clickable.")

    # Click the login button
    login_button.click()
    logging.info("Login button clicked.")

    # Close the driver
    driver.quit()
    logging.info("Driver closed.")

except NoSuchElementException as e:
    logging.error(f"Error occurred: {e}")
    logging.error("Failed to locate an element. Check the element identifiers (name, id, etc.).")
except Exception as e:
    logging.error(f"Error occurred: {e}")
    logging.error("An unexpected error occurred.")
