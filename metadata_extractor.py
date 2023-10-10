from bs4 import BeautifulSoup
import logging, os, sys, requests

# Set up logging
output_dir = "/home/chatgpt/custom_utilities/utility_library/tmp/metadata_extractor"
os.makedirs(output_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(output_dir, "metadata_extractor_log.txt"), level=logging.INFO)

def extract_metadata(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title = soup.title.string if soup.title else "No title found"

    # Extract standard, OpenGraph, and Twitter description
    description = get_meta_content(soup, ["description", "og:description", "twitter:description"])

    # Extract standard, OpenGraph, and Twitter keywords
    keywords = get_meta_content(soup, ["keywords", "og:keywords", "twitter:keywords"])

    # Extract additional metadata
    additional_metadata = {}
    for meta_tag in soup.find_all("meta"):
        if "name" in meta_tag.attrs and "content" in meta_tag.attrs:
            additional_metadata[meta_tag["name"]] = meta_tag["content"]

    metadata = {
        "title": title,
        "description": description,
        "keywords": keywords,
        "additional_metadata": additional_metadata
    }

    # Write metadata to output file
    with open(os.path.join(output_dir, "metadata_extractor_output.txt"), "w") as f:
        f.write(str(metadata))

    logging.info(f"Metadata for {url}: {metadata}")

def get_meta_content(soup, names):
    for name in names:
        tag = soup.find("meta", attrs={"name": name})
        if tag and "content" in tag.attrs:
            return tag["content"]
    return "No content found"

# Get URL from command-line argument
print(f"sys.argv: {sys.argv}")
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "http://example.com"

# Test the function
extract_metadata(url)
