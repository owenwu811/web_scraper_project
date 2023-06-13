import os
import requests
from bs4 import BeautifulSoup

output_dir = "/home/chatgpt/custom_utilities/utility_library/tmp/broken_link_checker_output"
log_file = output_dir + "/log.txt"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def log_message(message):
    with open(log_file, "a") as log:
        log.write(message + "\n")

def check_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a")
            broken_links = []
            for link in links:
                href = link.get("href")
                if href and href.startswith("http") and "//" in href:
                    link_response = requests.get(href)
                    if link_response.status_code != 200:
                        broken_links.append(href)
            with open(output_dir + "/output.txt", "w") as output_file:
                for broken_link in broken_links:
                    output_file.write(broken_link + "\n")
            log_message(f"Checked {len(links)} links, found {len(broken_links)} broken links.")
        else:
            log_message(f"Failed to retrieve page content. Status code: {response.status_code}")
    except Exception as e:
        log_message(f"An error occurred: {str(e)}")

check_links("https://docs.celonis.com/en/real-time-extension.html#UUID-340edb83-4d12-4304-d8ec-b7135b32e01c_section-idm4612699282545633418875580073")
