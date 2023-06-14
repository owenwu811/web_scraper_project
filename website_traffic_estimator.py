import os
import sys
import logging
import requests
from bs4 import BeautifulSoup

# Set up logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/website_traffic_estimator.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Set up output directory
output_dir = '/home/chatgpt/custom_utilities/utility_library/tmp/'

# Function to estimate website traffic
def estimate_traffic(domain):
    try:
        url = f'https://www.alexa.com/siteinfo/{domain}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        rank_div = soup.find('div', {'class': 'rankmini-rank'})
        rank = rank_div.text.strip() if rank_div else 'N/A'
        return rank
    except Exception as e:
        logging.error(f'Error estimating traffic for {domain}: {e}')
        return None

# Main function
if __name__ == '__main__':
    domain = sys.argv[1]
    rank = estimate_traffic(domain)
    if rank:
        output_filename = os.path.join(output_dir, f'{domain}_traffic_estimate.txt')
        with open(output_filename, 'w') as f:
            f.write(rank)
        logging.info(f'Traffic estimate for {domain} saved to {output_filename}')
    else:
        logging.error(f'Failed to estimate traffic for {domain}')
