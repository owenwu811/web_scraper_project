import requests
import sys
import os
import logging

# Setup logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/website_availability_checker.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Get website URL from command line argument
website_url = sys.argv[1]

try:
    response = requests.get(website_url)
    if response.status_code == 200:
        print(f'Website {website_url} is up.')
        logging.info(f'Website {website_url} is up.')
    else:
        print(f'Website {website_url} is down. Status code: {response.status_code}')
        logging.warning(f'Website {website_url} is down. Status code: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error checking website {website_url}: {e}')
    logging.error(f'Error checking website {website_url}: {e}')
