import requests
import json

# Nautobot API configuration
url = "https://demo.nautobot.com"
token = "a" * 40  # Replace with your actual token
headers = {"Authorization": f"Token {token}"}

# ------------------------------
# Step 1: Get devices (limit to 2)
# ------------------------------
response = requests.get(f"{url}/api/dcim/devices?limit=2", headers=headers)
devices = response.json().get("results", [])

for device in devices:
    device_name = device.get("name", "Unnamed")
    device_id = device.get("id")
    print(f"=== Device: {device_name} ===")

    # ------------------------------
    # Step 2: Get interfaces for this device (limit to 2)
    # ------------------------------
    response = requests.get(f"{url}/api/dcim/interfaces/?device_id={device_id}&limit=2", headers=headers)
    interfaces = response.json().get("results", [])

    for interface in interfaces:
        interface_name = interface.get("name", "Unnamed")
        interface_id = interface.get("id")
        print(f"--- Interface: {interface_name} ---")

        # ------------------------------
        # Step 2b: Get IP addresses for this interface
        # ------------------------------
        response = requests.get(f"{url}/api/ipam/ip-addresses/?interface_id={interface_id}", headers=headers)
        ip_addresses = response.json().get("results", [])
        if ip_addresses:
            print("IP Addresses:")
            for ip in ip_addresses:
                print(f"  - {ip.get('address', 'Unknown')}")
        else:
            print("IP Addresses: None")

        # ------------------------------
        # Step 3: Get trace for this interface
        # ------------------------------
        response = requests.get(f"{url}/api/dcim/interfaces/{interface_id}/trace", headers=headers)
        trace = response.json() if response.status_code == 200 else {}
        print("Trace:")
        print(json.dumps(trace, indent=4))
        print("="*50)

# ------------------------------
# Step 4: Get BGP peer endpoints
# ------------------------------
response = requests.get(f"{url}/api/plugins/bgp/peer-endpoints", headers=headers)
bgp_peer_endpoints = response.json().get("results", [])
if bgp_peer_endpoints:
    print("=== BGP Peer Endpoint Example ===")
    print(json.dumps(bgp_peer_endpoints[0], indent=4))
else:
    print("No BGP peer endpoints found.")
