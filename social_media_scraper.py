import sys
import requests
from bs4 import BeautifulSoup

# Get the URL from the command line arguments
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Add your scraping logic here

# For now, just print the title of the page
print(soup.title.string)
