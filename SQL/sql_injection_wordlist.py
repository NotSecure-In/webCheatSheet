import requests

# Function to check if a SQL injection vulnerability exists
def check_vulnerability(url, sql_file):
    # Load the SQL injection payloads from the file
    with open(sql_file, "r") as f:
        payloads = [line.strip() for line in f.readlines()]
    
    for payload in payloads:
        # Add the payload to the URL parameter
        attack_url = url + payload
        # Send the request to the server
        response = requests.get(attack_url)
        # Check if the response contains a SQL error message
        if "error in your SQL syntax" in response.text:
            print("SQL injection vulnerability found: " + attack_url)

# Example usage
target_url = "http://example.com/product?id=1"
sql_payloads_file = "sql_payloads.txt"
check_vulnerability(target_url, sql_payloads_file)
