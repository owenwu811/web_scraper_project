import sys, logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up logging
logging.basicConfig(filename='/home/chatgpt/custom_utilities/utility_library/tmp/image_scraper.log', level=logging.INFO)

def scrape_images(url):
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Set path to chromedriver as per your configuration
        webdriver_service = Service('/usr/bin/chromedriver')

        # Initialize webdriver
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

        # Open URL
        driver.get(url)

        # Find images
        images = driver.find_elements(By.TAG_NAME, 'img')

        # Print image URLs
        for image in images:
            print(image.get_attribute('src'))

        driver.quit()

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        logging.error(f"Exception type: {type(e)}")
        logging.error(f"Exception args: {e.args}")
        logging.error("Exception traceback:", exc_info=True)

if __name__ == "__main__":
    url = sys.argv[1]
    scrape_images(url)
