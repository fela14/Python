import json
import requests
from requests.auth import HTTPBasicAuth
from unittest.mock import patch, MagicMock

if __name__ == "__main__":
    # requests class to create the basic authentication header
    auth = HTTPBasicAuth('ntc', 'ntc123')
    url = 'http://eos-spine1/command-api'

    # payload expected by the API
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
            "cmds": [
                "show vlan brief"
            ],
            "version": 1
        },
        "id": "EapiExplorer-1"
    }

    # 👇 Mock requests.post so no real device is needed
    with patch("requests.post") as mock_post:
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            "jsonrpc": "2.0",
            "id": "EapiExplorer-1",
            "result": [{
                "vlans": {
                    "1": {"name": "default", "status": "active"},
                    "10": {"name": "Users", "status": "active"},
                    "20": {"name": "Servers", "status": "active"}
                }
            }]
        }
        mock_post.return_value = fake_response

        # Make the request (actually uses the mock above)
        response = requests.post(
            url,
            data=json.dumps(payload),
            auth=auth,
            headers={"Content-Type": "application/json"}
        )

        # Helper output onscreen to show the status code and response
        print(f'STATUS CODE: {response.status_code}')
        print(f'RESPONSE: {json.dumps(response.json(), indent=4)}')


#########################################################################################################

# Using eAPI to autoconfigure interface descriptions based on LLDP data

import json
import sys
import requests
from requests.auth import HTTPBasicAuth

# Helper method to issue "commands" to a "device", and return the result
def issue_request(device, commands):
    """Make API request to EOS device returning JSON response."""
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
            "cmds": commands,
            "version": 1
        },
        "id": "EapiExplorer-1"
    }
    response = requests.post(
        'http://{}/command-api'.format(device),
        data=json.dumps(payload),
        auth=HTTPBasicAuth('ntc', 'ntc123')
    )
    return response.json()


def get_lldp_neighbors(device):
    """Get list of neighbors
    Sample response for a single neighbor:
    {
        "ttl": 120,
        "neighborDevice": "eos-spine2.ntc.com",
        "neighborPort": "Ethernet2",
        "port": "Ethernet2"
    }
    """
    # Define the target methods
    commands = ['show lldp neighbors']
    response = issue_request(device, commands)
    # Extract the neighbors' data from the result of the first and only command
    # and return it as a list of dictionaries
    return response['result'][0]['lldpNeighbors']


def configure_interfaces(device, neighbors):
    """Configure interfaces in a single API call per device."""
    command_list = ['enable', 'configure']
    for neighbor in neighbors:
        local_interface = neighbor['port']
        if local_interface.startswith('Eth'):
            # Excluding Management as it has multiple neighbors
            description = (
                f"Connects to interface {neighbor['neighborPort']} on neighbor "
                f"{neighbor['neighborDevice']}"
            )
            description = 'description ' + description
            interface = f'interface {local_interface}'
            # Extending the list of commands, in the proper order
            command_list.extend([interface, description])
    # Retrieve the output from the commands created from the neighbors
    response = issue_request(device, command_list)


if __name__ == "__main__":
    # device names are FQDNs
    devices = ['eos-spine1', 'eos-spine2']
    for device in devices:
        neighbors = get_lldp_neighbors(device)
        configure_interfaces(device, neighbors)
        print('Auto-configured Interfaces for {}'.format(device))
