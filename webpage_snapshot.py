import sys
import imgkit

# Get the URL from the command line arguments
url = sys.argv[1]

# Configure options for imgkit
options = {
    "format": "png",
    "encoding": "UTF-8"
}

# Create a screenshot of the webpage
imgkit.from_url(url, "/home/chatgpt/custom_utilities/utility_library/tmp/webpage_snapshot.png", options=options)
