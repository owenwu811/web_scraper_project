import os
import sys
import time
import logging
import requests
from python_anticaptcha import AnticaptchaClient, ImageToTextTask

# Set up logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/captcha_solver.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Set up output directory
output_dir = '/home/chatgpt/custom_utilities/utility_library/tmp/'

# Function to solve CAPTCHA
def solve_captcha(api_key, captcha_file):
    try:
        client = AnticaptchaClient(api_key)
        with open(captcha_file, 'rb') as f:
            task = ImageToTextTask(f)
            job = client.createTask(task)
            job.join()
        return job.get_captcha_text()
    except Exception as e:
        logging.error(f'Error solving CAPTCHA: {e}')
        return None

# Main function
if __name__ == '__main__':
    api_key = os.environ.get('ANTI_CAPTCHA_API_KEY')
    captcha_file = sys.argv[1]
    captcha_text = solve_captcha(api_key, captcha_file)
    if captcha_text:
        output_filename = os.path.join(output_dir, 'captcha_solution.txt')
        with open(output_filename, 'w') as f:
            f.write(captcha_text)
        logging.info(f'Captcha solution saved to {output_filename}')
    else:
        logging.error('Failed to solve CAPTCHA')
