# Flow control within loops

vendors = ['arista', 'juniper', 'cisco']

for index, vendor in enumerate(vendors):
    print('{}: {}'.format(index,vendor))

vendors = ['arista', 'juniper', 'cisco']
for index, each in enumerate(vendors):
   print(index)
   if each == 'arista':
       print(f'arista index is: {index}')
       break

# Using python functions

devices = ['switch1', 'switch2', 'switch3']
vlans = [
    {'id': '10', 'name': 'MGT'},
    {'id': '20', 'name': 'SALES'},
    {'id': '30', 'name': 'VOICE'},]


from push import push_commands
from get import get_commands

# print(help(get_commands))
for vlan in vlans:
    vid = vlan.get('id')
    name = vlan.get('name')
    print(f'CONFIGURING VLAN: {vid}')
    commands = get_commands(vid, name)
    for device in devices:
        push_commands(device, commands)

vlans_list = ['vlan 10', ' name USERS', 'vlan 20', ' name VOICE', 'vlan 30',
' name WLAN', 'vlan 40', ' name APP', 'vlan 50', ' name WEB',
'vlan 60', ' name DB']

for item in vlans_list:
    
    if 'vlan' in item:
        temp = {}
        id = item.strip().strip('vlan').strip()
        temp['id'] = id
    elif 'name' in item:
        name = item.strip().strip('name').strip()
        temp['name'] = name
        vlans.append(temp)    
print(vlans)

""" vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}, {'id': '40', 'name': 'APP'},
{'id': '50', 'name': 'WEB'}, {'id': '60', 'name': 'DB'}]

new_vlan = {'id': '70', 'name': 'DEV'}
add_vlan = {'id': '70', 'name': 'HQ'}
vlans.append(new_vlan)
vlans.append(add_vlan)
print(vlans)

write_file = open('vlan_new.cfg', 'w')
for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
    write_file.write(f'vlan {id}\n')
    write_file.write(f'  name {name}\n')
"""
import time

def run_task(vlans):
    start_time = time.time()
    for vlan in vlans:
        result = get_commands(vlan=vlan['id'], name=vlan['name'])
        print(result)
    print(f'Time spent: {time.time() - start_time} seconds')

run_task(vlans)

import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:
    start_time = time.time()
    tasks = []
    for vlan in vlans:
        tasks.append(
            executor.submit(
                get_commands, vlan=vlan['id'], name=vlan['name']  
            )
        )
    for task in concurrent.futures.as_completed(tasks):
        print(task.result())
    print(f'Time spent: {time.time() - start_time} seconds')

run_task(vlans)

