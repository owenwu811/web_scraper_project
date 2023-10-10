import requests, hashlib, time, sys, logging

# Setup logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/content_change_detector.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Get website URL from command line argument
website_url = sys.argv[1]

# Initial hash value
hash_value = ''

while True:
    try:
        # Send a GET request to the website
        response = requests.get(website_url)

        # Calculate the hash of the website content
        new_hash_value = hashlib.md5(response.content).hexdigest()

        # If the hash value has changed, log a message
        if new_hash_value != hash_value:
            logging.info(f'Content change detected on {website_url}')
            hash_value = new_hash_value

        # Wait before checking again
        time.sleep(60)

    except requests.exceptions.RequestException as e:
        # If there's an exception, log an error message
        logging.error(f'Error sending request to {website_url}: {e}')
