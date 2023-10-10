import os, sys, logging, time, requests

# Set up logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/adaptive_scraping.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Set up output directory
output_dir = '/home/chatgpt/custom_utilities/utility_library/tmp/'

# Function to make a GET request with adaptive delay
def adaptive_get(url, min_delay=1, max_delay=5):
    delay = min_delay
    while True:
        try:
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time
            if response.status_code == 200:
                return response
            elif response.status_code == 429:
                delay = min(max_delay, delay * 2)
                logging.info(f'Received 429 Too Many Requests, increasing delay to {delay} seconds')
            else:
                logging.error(f'Received status code {response.status_code}')
                return None
        except Exception as e:
            logging.error(f'Error making GET request: {e}')
            return None
        finally:
            time.sleep(delay)

# Main function
if __name__ == '__main__':
    url = sys.argv[1]
    response = adaptive_get(url)
    if response:
        output_filename = os.path.join(output_dir, 'adaptive_scraping_response.txt')
        with open(output_filename, 'w') as f:
            f.write(response.text)
        logging.info(f'Response saved to {output_filename}')
    else:
        logging.error('Failed to make GET request')
