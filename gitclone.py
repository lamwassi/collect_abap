import os
import json
# # Replace the URL with the URL of the GitHub repository you want to clone
# url = "https://github.com/abapGit/abapGit"

# # Replace "path/to/destination" with the path where you want to clone the repository
# destination = "/app/abap2"

# # Clone the repository
# os.system(f"git clone {url} {destination}")



import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to retrieve
url = "https://github.com/search?q=abap+language%3AABAP&type=repositories"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all <a> tags in the HTML content
d_tags = soup.find_all("a")
repos = []
# Loop through each <a> tag and extract its href attribute
for a_tag in d_tags:
    href = a_tag.get("href")
    if href is not None:
        split_href = href.split("/")
        if len(split_href) == 3:  
            print(split_href)
            # Check if the URL is a valid GitHub repository by sending a GET request to the GitHub API endpoint
            api_url = f"https://api.github.com/repos/{href}"
            response = requests.get(api_url)
            if response.status_code == 200:
                print("This is a valid GitHub repository.")
                repos.append(href)    
                print(href)   
            else: 
                print("{}: is nat a valid repo".format(href))    
with open("page1_repos.json", "w", encoding="utf-8") as rep:
    rep.write(json.dumps(rep , indent=4))
    
    
    
    
   