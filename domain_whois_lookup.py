import os
import sys
import whois
import logging
from datetime import datetime

# Set up logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/domain_whois_lookup.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Set up output directory
output_dir = '/home/chatgpt/custom_utilities/utility_library/tmp/'

# Function to perform WHOIS lookup
def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        logging.error(f'Error performing WHOIS lookup for {domain}: {e}')
        return None

# Main function
if __name__ == '__main__':
    domain = sys.argv[1]
    result = whois_lookup(domain)
    if result:
        output_filename = os.path.join(output_dir, f'{domain}_whois.txt')
        with open(output_filename, 'w') as f:
            f.write(str(result))
        logging.info(f'WHOIS lookup result for {domain} saved to {output_filename}')
    else:
        logging.error(f'Failed to perform WHOIS lookup for {domain}')
