import requests
import urllib.request
import time
from bs4 import BeautifulSoup

URL = 'https://www.vox.com/'
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

#results = soup.find_("h2", class="c-entry-box--compact__body")
#print(results)

print(soup.find_all("h2"))
