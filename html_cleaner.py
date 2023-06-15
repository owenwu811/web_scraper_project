import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import sys

# URL to clean HTML
url = sys.argv[1]

# Parse HTML with BeautifulSoup
def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove unnecessary tags
    for tag in soup(["script", "style"]):
        tag.decompose()

    # Remove comments
    comments = soup.findAll(string=lambda text:isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    return soup.prettify()

if __name__ == "__main__":
    html = requests.get(url).text
    clean_html = clean_html(html)
    with open("/home/chatgpt/custom_utilities/utility_library/tmp/html_cleaner_output.txt", "w") as file:
        file.write(clean_html)
