import requests
from bs4 import BeautifulSoup
import os
import logging
import sys
from textblob import TextBlob

# Set up logging
output_dir = "/home/chatgpt/custom_utilities/utility_library/tmp/sentiment_analyzer"
os.makedirs(output_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(output_dir, "sentiment_analyzer_log.txt"), level=logging.INFO)

def analyze_sentiment(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract text content
    text_content = soup.get_text()

    # Analyze sentiment
    blob = TextBlob(text_content)
    sentiment = blob.sentiment

    # Write sentiment to output file
    with open(os.path.join(output_dir, "sentiment_analyzer_output.txt"), "w") as f:
        f.write(str(sentiment))

    logging.info(f"Sentiment for {url}: {sentiment}")

# Get URL from command-line argument
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "http://example.com"

# Test the function
analyze_sentiment(url)
