from pygnmi.client import gNMIclient
import json

# Replace these values with your Cisco device details
device_ip = "10.10.20.30"        # Cisco device IP address
gnmi_port = 57400                # Default Cisco gNMI port
username = "cisco"               # Your device username
password = "cisco123"            # Your device password

with gNMIclient(
    target=(device_ip, gnmi_port),
    username=username,
    password=password,
    insecure=True   # Keep True for lab/testing if no TLS cert
) as gnmi:
    result = gnmi.get(path=[
        'openconfig-interfaces:interfaces',
        'openconfig-acl:acl'
    ])

# Print in readable JSON format
print(json.dumps(result, indent=2))

