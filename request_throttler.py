import os, sys, time, logging, requests
# Set up logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/request_throttler.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Set up output directory
output_dir = '/home/chatgpt/custom_utilities/utility_library/tmp/'

# Function to make throttled requests
def throttled_request(url, delay):
    try:
        time.sleep(delay)
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        logging.error(f'Error making request to {url}: {e}')
        return None

# Main function
if __name__ == '__main__':
    url = sys.argv[1]
    delay = float(sys.argv[2])
    status_code = throttled_request(url, delay)
    if status_code:
        safe_url = url.replace('/', '_').replace(':', '')
        output_filename = os.path.join(output_dir, f'{safe_url}_status_code.txt')
        with open(output_filename, 'w') as f:
            f.write(str(status_code))
        logging.info(f'Status code for {url} saved to {output_filename}')
    else:
        logging.error(f'Failed to make request to {url}')
