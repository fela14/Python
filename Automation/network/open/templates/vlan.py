from jinja2 import Environment, FileSystemLoader

"""
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("vlan.j2")


 
interface_dict = {
    "name": "GigabitEthernet2",
    "description": "Uplink",
    "vlan": 10,
    "uplink": False
}

print(template.render(interface=interface_dict))

class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=True):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

interface = NetworkInterface("GigabitEthernet2", "Server Port", 10)

# Pass it with the exact variable name the template expects
print(template.render(interface=interface))

intlist = [
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "GigabitEthernet0/3"
]
print(template.render(interface_list=intlist)) 

intdict = {
    "GigabitEthernet0/1": "Server port number one",
    "GigabitEthernet0/2": "Server port number two",
    "GigabitEthernet0/3": "Server port number three"
}
print(template.render(interface_dict=intdict)) 
interfaces = [
    {
    "name": "GigabitEthernet0/1",
    "desc": "uplink port",
    "uplink": True
    },
    {
    "name": "GigabitEthernet0/2",
    "desc": "Server port number one",
    "vlan": 10
    },
    {
    "name": "GigabitEthernet0/3",
    "desc": "Server port number two",
    "vlan": 10
    },
    {
    "name": "GigabitEthernet0/4"
    },
    {
    "desc": "Server port number two",
    }
]

print(template.render(interface_list=interfaces)) """
import os
import yaml
from jinja2 import Environment, FileSystemLoader

# --- Custom Filters ---
def get_interface_speed(interface_name):
    """Returns default Mbps value for a given interface name"""
    if not interface_name:
        return 10
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100
    return 10

def reverse_string(value):
    """Reverse a string"""
    return value[::-1]

# --- Setup Environment ---
template_dir = os.path.dirname(__file__)   # current script's folder
ENV = Environment(loader=FileSystemLoader(template_dir))

# Register filters
ENV.filters['get_interface_speed'] = get_interface_speed
ENV.filters['reverse'] = reverse_string

# Debug: confirm filters exist
print("Filters registered:", list(ENV.filters.keys()))

# --- Load Template ---
template = ENV.get_template('yes-http.j2')

# --- Load YAML ---
yaml_file = os.path.join(template_dir, "vlan.yml")
with open(yaml_file) as f:
    interfaces = yaml.safe_load(f)

# --- Extra dict for testing lookup ---
sw01 = {
    "config": {
        "interfaces": {
            "ge0/1": {"description": "Uplink to Core"},
            "ge0/2": {"description": "Server LAN"}
        }
    }
}

# --- Render once with everything ---
print(template.render(interface_list=interfaces, sw01=sw01))
