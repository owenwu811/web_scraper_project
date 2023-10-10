import requests, random, logging
# Setup logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/user_agent_rotator.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# List of user agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
]

# Get website URL from command line argument
website_url = sys.argv[1]

try:
    # Choose a random user agent
    user_agent = random.choice(user_agents)

    # Send a GET request with the user agent
    headers = {'User-Agent': user_agent}
    response = requests.get(website_url, headers=headers)

    if response.status_code == 200:
        print(f'Successfully sent request to {website_url} with user agent {user_agent}')
        logging.info(f'Successfully sent request to {website_url} with user agent {user_agent}')
    else:
        print(f'Failed to send request to {website_url} with user agent {user_agent}. Status code: {response.status_code}')
        logging.warning(f'Failed to send request to {website_url} with user agent {user_agent}. Status code: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error sending request to {website_url} with user agent {user_agent}: {e}')
    logging.error(f'Error sending request to {website_url} with user agent {user_agent}: {e}')
