import requests
from bs4 import BeautifulSoup

# The URL to test for XSS vulnerabilities
url = "https://example.com/"

# The path to your custom wordlist containing payloads to test for XSS vulnerabilities
wordlist_path = "/path/to/your/wordlist.txt"

# Read the payloads from the wordlist file
with open(wordlist_path, "r") as f:
    xss_wordlist = [line.strip() for line in f.readlines()]

# Retrieve the page content and extract the parameters from all the links and forms
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a")
forms = soup.find_all("form")
params = set()

for link in links:
    url_parts = link["href"].split("?")
    if len(url_parts) > 1:
        params.update(url_parts[1].split("&"))

for form in forms:
    params.update(form.find_all("input", attrs={"name": True}))

# Test each parameter with your custom wordlist
for param in params:
    param_name = param.split("=")[0]
    for payload in xss_wordlist:
        url_with_payload = url.replace(param, f"{param_name}={payload}")
        response_with_payload = requests.get(url_with_payload)
        if payload in response_with_payload.text:
            print(f"XSS vulnerability found in parameter: {param_name}")
            print(f"Payload: {payload}")
            print(f"URL: {url_with_payload}")
            break
