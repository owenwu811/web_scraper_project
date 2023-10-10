import requests, itertools, logging
from datetime import datetime

# Setup logging
log_file = '/home/chatgpt/custom_utilities/utility_library/tmp/proxy_rotator.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# List of proxies
proxies = [
    'http://proxy1.com:8080',
    'http://proxy2.com:8080',
    'http://proxy3.com:8080',
    # Add more proxies as needed
]

# Create an iterator that cycles through the proxies
proxy_pool = itertools.cycle(proxies)

# Function to make a request using a proxy from the pool
def make_request(url):
    for i in range(1, len(proxies) + 1):
        # Get the next proxy from the pool
        proxy = next(proxy_pool)
        logging.info(f'Trying proxy: {proxy}')
        try:
            response = requests.get(url, proxies={'http': proxy, 'https': proxy})
            return response.content
        except Exception as e:
            logging.error(f'Error occurred: {e}')
            logging.info(f'Retrying with next proxy')
    logging.error('All proxies failed')
    return None

# Main function
if __name__ == '__main__':
    url = 'http://example.com'
    content = make_request(url)
    if content:
        logging.info(f'Successfully retrieved content from {url}')
    else:
        logging.error('Failed to retrieve content')
