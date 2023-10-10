import requests, sys, logging
# Setup logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/cookie_handler.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Get website URL from command line argument
website_url = sys.argv[1]

try:
    # Send a GET request to the website
    response = requests.get(website_url)

    # Get the cookies from the response
    cookies = response.cookies

    # Log the cookies
    logging.info(f'Cookies for {website_url}: {cookies}')

    # Print a success message
    print(f'Successfully retrieved cookies for {website_url}')

except requests.exceptions.RequestException as e:
    # Print and log an error message if there's an exception
    print(f'Error retrieving cookies for {website_url}: {e}')
    logging.error(f'Error retrieving cookies for {website_url}: {e}')
