import requests, random

# List of referrers
referrers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.facebook.com/",
    "https://www.reddit.com/"
]

def get_page_with_referrer(url):
    try:
        # Choose a random referrer
        referrer = random.choice(referrers)

        headers = {
            "Referer": referrer
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Received status code {response.status_code}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    url = "http://example.webscraping.com/"
    print(get_page_with_referrer(url))
