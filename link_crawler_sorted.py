import requests
from bs4 import BeautifulSoup
import re
import sys
import os

def get_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong... Exiting.",err)
        sys.exit()

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def filter_links(links, url):
    filtered_links = []
    for link in links:
        if link.lower().endswith(('.html', '.htm', '.xls', '.xlsx', '.csv')) or re.search(r'\d{4}\d{2}', link):
            if link.startswith('http') or link.startswith('www'):
                filtered_links.append(link)
            else:
                filtered_links.append(url + link)
    return filtered_links

def write_links_to_file(links, filename):
    with open(filename, 'w') as f:
        for link in links:
            f.write("%s\n" % link)

def main():
    url = sys.argv[1]
    links = get_links(url)
    links = filter_links(links, url)
    filename = os.path.join('/home/chatgpt/custom_utilities/utility_library/tmp/link_crawler_sorted', 'output.txt')
    write_links_to_file(links, filename)

if __name__ == "__main__":
    main()
