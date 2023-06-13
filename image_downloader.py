import os
import requests
from bs4 import BeautifulSoup
import logging
import sys
import base64
from urllib.parse import urljoin

# Set up logging
dir_path = "/home/chatgpt/custom_utilities/utility_library/tmp/image_downloader"
logging.basicConfig(filename=os.path.join(dir_path, "image_downloader.log"), level=logging.INFO)

def download_images(url):
    try:
        # Delete the contents of the image_web_server directory
        for filename in os.listdir(os.path.join(dir_path, "image_web_server")):
            os.remove(os.path.join(dir_path, "image_web_server", filename))
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # Find all image tags
        img_tags = soup.find_all("img")
        # For each image tag, download the image and save it to the directory
        for img in img_tags:
            img_url = img.get("src")
            # Convert relative URLs to absolute URLs
            img_url = urljoin(url, img_url)
            if "data:image" in img_url:
                # If the image is a data URL, decode the data URL
                img_data = base64.b64decode(img_url.split(",", 1)[1])
            else:
                # Otherwise, send a GET request to the image URL
                img_data = requests.get(img_url).content
            img_file = os.path.join(dir_path, "image_web_server", os.path.basename(img_url.split("/", -1)[-1]))
            with open(img_file, "wb") as f:
                f.write(img_data)
            logging.info(f"Downloaded image {img_file}")
        # Write the image URLs to a text file
        with open(os.path.join(dir_path, "image_urls.txt"), "w") as f:
            for img in img_tags:
                img_url = img.get("src")
                img_url = urljoin(url, img_url)
                f.write(f"http://<your-server-ip>:8000/{os.path.basename(img_url.split(\"/\", -1)[-1])}\n")
    except Exception as e:
        logging.error(f"Error downloading images: {e}")

if __name__ == "__main__":
    url = sys.argv[1]
    download_images(url)

