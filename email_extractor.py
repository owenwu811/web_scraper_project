import os, re, requests
from bs4 import BeautifulSoup

output_dir = "/home/chatgpt/custom_utilities/utility_library/tmp/email_extractor_output"
log_file = os.path.join(output_dir, "log.txt")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def log_message(message):
    with open(log_file, "a") as log:
        log.write(message + "\n")

def extract_emails(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            email_addresses = re.findall(r"[a-z0-9\.\-_]+@[a-z0-9\.\-_]+\.[a-z]+", soup.text, re.I)
            with open(os.path.join(output_dir, "output.txt"), "w") as output_file:
                for email in email_addresses:
                    output_file.write(email + "\n")
            log_message(f"Successfully extracted {len(email_addresses)} email addresses from {url}")
        else:
            log_message(f"Failed to retrieve page content. Status code: {response.status_code}")
    except Exception as e:
        log_message(f"An error occurred: {str(e)}")

extract_emails("https://10minutemail.com/")
