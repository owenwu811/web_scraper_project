import argparse, logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin

# Set up logging
logging.basicConfig(filename='/home/chatgpt/custom_utilities/utility_library/tmp/link_extractor.log', level=logging.INFO)

def extract_links(url):
    try:
        logging.info("Setting up Chrome options...")
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Set path to chromedriver as per your configuration
        webdriver_service = Service('/usr/bin/chromedriver')

        logging.info("Launching Chrome browser...")
        # Choose Chrome Browser
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

        logging.info(f"Navigating to {url}...")
        driver.get(url)

        logging.info("Extracting links...")
        elements = driver.find_elements(By.TAG_NAME, "a")

        links = [urljoin(url, element.get_attribute("href")) for element in elements]

        logging.info("Writing links to output file...")
        with open('/home/chatgpt/custom_utilities/utility_library/tmp/link_extractor_output.txt', 'w') as f:
            for link in links:
                f.write(link + "\n")

        driver.quit()

        logging.info("Successfully extracted links.")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract links from a given URL.')
    parser.add_argument('url', help='The URL to extract links from.')

    args = parser.parse_args()

    extract_links(args.url)
