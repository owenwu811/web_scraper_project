import os, sys, time, logging, requests
# Set up logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/page_load_speed_tester.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Set up output directory
output_dir = '/home/chatgpt/custom_utilities/utility_library/tmp/'

# Function to test page load speed
def test_page_load_speed(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        load_time = time.time() - start_time
        if response.status_code == 200:
            return load_time
        else:
            logging.error(f'Received status code {response.status_code}')
            return None
    except Exception as e:
        logging.error(f'Error testing page load speed: {e}')
        return None

# Main function
if __name__ == '__main__':
    url = sys.argv[1]
    load_time = test_page_load_speed(url)
    if load_time is not None:
        output_filename = os.path.join(output_dir, 'page_load_speed.txt')
        with open(output_filename, 'w') as f:
            f.write(str(load_time))
        logging.info(f'Page load speed saved to {output_filename}')
    else:
        logging.error('Failed to test page load speed')
