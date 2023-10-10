import requests, json, sys, os, logging
from datetime import datetime

# Setup logging
log_file = '/home/chatgpt/custom_utilities/utility_library/tmp/domain_info.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Output file
output_file = '/home/chatgpt/custom_utilities/utility_library/tmp/domain_info_output.txt'

# Function to get domain info
def get_domain_info(domain):
    try:
        response = requests.get(f'https://api.whois.vu/?q={domain}')
        data = response.json()
        return data
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        return None

# Main function
if __name__ == '__main__':
    domain = sys.argv[1]
    info = get_domain_info(domain)
    if info:
        with open(output_file, 'w') as f:
            f.write(json.dumps(info, indent=4))
        logging.info(f'Domain info saved to {output_file}')
    else:
        logging.error('Failed to retrieve domain info')
