#!/usr/bin/env python3


import requests
import sys
from bs4 import BeautifulSoup

# Check if the URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python ./main.py <Google Forms URL>")
    sys.exit(1)

# Get the URL from the command-line argument
url = sys.argv[1]

# Fetch the content of the URL
response = requests.get(url)

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the meta tag with the property "og:image"
meta_tag = soup.find("meta", property="og:image")
if meta_tag:
    old_content = meta_tag.get("content")
    # Replace the specified part of the content
    new_content = old_content.replace("w1200-h630-p", "w900-h1300-p")
    # Print the new content
    print(new_content)
else:
    print("No meta tag with property 'og:image' found.")
