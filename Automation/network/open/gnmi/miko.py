from netmiko import ConnectHandler

device = ConnectHandler(
    host='10.10.20.48',
    username='developer',
    password='C1sco12345',
    device_type='cisco_iosxe'
)

print(dir(device))
print(device.find_prompt())

device.config_mode()
print(device.find_prompt())

show_run_output = device.send_command('show_run')
print(show_run_output[:176])

output = device.send_command_expect('end', expect_string='cisco-iosxe#')
output = device.send_command_timing('end')

commands = [
    'interface Ethernet1/1',
    'description configured by netmiko',
    'shutdown'
]

device.config_mode()
output = device.send_config_set(config_commands=commands)
print(output)

from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

device = ConnectHandler(
    host= "10.10.20.47",
    username= "developer",
    password= "C1sco12345",
    device_type= "cisco_iosxe"
)

interface_dict = {
    "name": "GigabitEthernet1/0",
    "description": "Server Port",
    "vlan": 10,
    "uplink": False
}

ENV = Environment(Loader=FileSystemLoader('.'))
template = ENV.get_template("cisco.j2")
commands = template.render(interface=interface_dict)

filename = "cisco.conf"
with open(filename, 'w') as cisco:
    cisco.writelines(commands)

output = device.send_config_from_file(filename)
verification = device.send_command(f'show run interface {interface_dict['name']}')
print(verification)

device.disconnect()

#  Using NTC Templates to get structured data from Netmiko output

from netmiko import ConnectHandler

device = ConnectHandler(
    host='10.10.20.48',
    username='developer',
    password='C1sco12345',
    device_type='cisco_iosxe'
)
show_interfaces_raw = device.send_command('show int brief')
print(show_interfaces_raw[:150])

from ntc_templates.parse import parse_output

show_interfaces_parsed = parse_output(
    platform="cisco_iosxe",
    command="show int brief",
    data=show_interfaces_raw,
)
print(show_interfaces_parsed[0])

show_interfaces_parsed_directly = device.send_command(
    'show int brief',
    use_textfsm=True)

print(show_interfaces_parsed == show_interfaces_parsed_directly)