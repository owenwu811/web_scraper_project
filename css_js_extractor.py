import requests, os, logging, sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set up logging
output_dir = "/home/chatgpt/custom_utilities/utility_library/tmp/css_js_extractor"
os.makedirs(output_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(output_dir, "css_js_extractor_log.txt"), level=logging.INFO)

def extract_css_js(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract CSS and JS files
    css_js_files = []
    for link in soup.find_all("link", rel="stylesheet"):
        if "href" in link.attrs:
            css_js_files.append(urljoin(url, link["href"]))
    for script in soup.find_all("script"):
        if "src" in script.attrs:
            css_js_files.append(urljoin(url, script["src"]))

    # Write CSS and JS files to output file
    with open(os.path.join(output_dir, "css_js_extractor_output.txt"), "w") as f:
        for file in css_js_files:
            f.write(file + "\n")

    logging.info(f"CSS and JS files for {url}: {css_js_files}")

# Get URL from command-line argument
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "http://example.com"

# Test the function
extract_css_js(url)
