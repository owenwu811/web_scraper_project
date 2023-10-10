import os, sys, logging, requests
from bs4 import BeautifulSoup

# Set up logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/page_rank_checker.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Set up output directory
output_dir = '/home/chatgpt/custom_utilities/utility_library/tmp/'

# Function to check Google PageRank
def check_page_rank(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(f'https://www.google.com/search?q=site:{url}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        result_div = soup.find('div', {'id': 'result-stats'})
        result = result_div.text if result_div else 'N/A'
        return result
    except Exception as e:
        logging.error(f'Error checking PageRank for {url}: {e}')
        return None

# Main function
if __name__ == '__main__':
    url = sys.argv[1]
    result = check_page_rank(url)
    if result:
        output_filename = os.path.join(output_dir, f'{url}_page_rank.txt')
        with open(output_filename, 'w') as f:
            f.write(result)
        logging.info(f'PageRank for {url} saved to {output_filename}')
    else:
        logging.error(f'Failed to check PageRank for {url}')
