import requests
from bs4 import BeautifulSoup
import os
import logging
import sys
from urllib.parse import urljoin, urlparse

# Set up logging
output_dir = "/home/chatgpt/custom_utilities/utility_library/tmp/link_crawler_sorted"
os.makedirs(output_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(output_dir, "link_crawler_sorted_log.txt"), level=logging.INFO)

def crawl_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract links
    links = []
    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"])
        try:
            response = requests.head(link)
            if 'content-type' in response.headers:
                content_type = response.headers['content-type']
                if 'application/vnd.ms-excel' in content_type or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type or 'text/csv' in content_type:
                    links.append(link)
        except requests.RequestException:
            pass  # Ignore errors

    # Write links to output file
    with open(os.path.join(output_dir, "link_crawler_sorted_output.txt"), "w") as f:
        for link in sorted(links):
            f.write(link + "\n")

    logging.info(f"Links for {url}: {links}")

# Get URL from command-line argument
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "http://example.com"

# Test the function
crawl_links(url)
