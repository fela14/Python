from jinja2 import Environment, FileSystemLoader

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
