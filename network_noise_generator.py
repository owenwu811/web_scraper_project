import requests
import random
import time

# List of URLs to generate network noise
urls = [
    "https://webscraper.io/test-sites",
    "https://www.scrapethissite.com/pages/",
    "https://proxyway.com/guides/best-websites-to-practice-your-web-scraping-skills"
]

def generate_noise():
    try:
        # Choose a random URL
        url = random.choice(urls)

        # Make a request to the URL
        response = requests.get(url)

        # Wait for a random amount of time
        time.sleep(random.randint(1, 5))

        if response.status_code == 200:
            return f"Noise generated with request to {url}"
        else:
            return f"Error: Received status code {response.status_code} when generating noise with request to {url}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(generate_noise())
