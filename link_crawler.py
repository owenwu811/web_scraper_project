import requests, os, logging, sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Set up logging
output_dir = "/home/chatgpt/custom_utilities/utility_library/tmp/link_crawler"
os.makedirs(output_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(output_dir, "link_crawler_log.txt"), level=logging.INFO)

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
        links.append(link)

    # Write links to output file
    with open(os.path.join(output_dir, "link_crawler_output.txt"), "w") as f:
        for link in links:
            f.write(link + "\n")

    logging.info(f"Links for {url}: {links}")

# Get URL from command-line argument
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "http://example.com"

# Test the function
crawl_links(url)
