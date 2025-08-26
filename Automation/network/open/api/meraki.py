
import requests
import json

API_KEY = "50acc8561d02bca8363bc2e0acb4a91e4eaab5a4"  # e.g., ending with b5a4
BASE_URL = "https://api.meraki.com/api/v1"

headers = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(f"{BASE_URL}/organizations", headers=headers)

print(response.status_code)           # should now be 200
print(json.dumps(response.json(), indent=2))  # readable JSON

organizations = response.json()
print(type(organizations))
print(organizations[0]['name'])

first_organization_id = organizations[0]["id"]
response = requests.get(f"{BASE_URL}/organizations/{first_organization_id}/networks", headers=headers)

networks = response.json()
print(networks)

#--- Create a Meraki network ---

payload = {
    "name": "my brand new automated network",
    "productTypes": ["switch"]
}

response = requests.post(f"{BASE_URL}/organizations/{first_organization_id}/networks", header=headers, data=json.dumps(payload))
# print(response.json())


