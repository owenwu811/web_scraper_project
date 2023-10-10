import requests, sys, time, logging

# Setup logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/dynamic_scraping_strategy.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Get website URL from command line argument
website_url = sys.argv[1]

# Initial wait time between requests
wait_time = 1

while True:
    try:
        # Send a GET request to the website
        response = requests.get(website_url)

        # If the response status code is 200, log a success message
        if response.status_code == 200:
            logging.info(f'Successfully sent request to {website_url}')

        # If the response status code is 429 (Too Many Requests), increase the wait time and log a warning
        elif response.status_code == 429:
            wait_time *= 2
            logging.warning(f'Too many requests to {website_url}. Increasing wait time to {wait_time} seconds.')

        # If the response status code is anything else, log a warning
        else:
            logging.warning(f'Unexpected status code {response.status_code} when sending request to {website_url}')

        # Wait before sending the next request
        time.sleep(wait_time)

    except requests.exceptions.RequestException as e:
        # If there's an exception, log an error message
        logging.error(f'Error sending request to {website_url}: {e}')
