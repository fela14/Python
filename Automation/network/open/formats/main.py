import yaml

with open("data.yaml") as d:
    result = yaml.load(d, Loader=yaml.FullLoader)
    print(result, type(result))
    
data = """
<devices>
    <device name="sw01">
        <vendor>Cisco</vendor>
        <model>Nexus 7700</model>
        <osver>NXOS 6.1</osver>
    </device>
    <device name="sw02">
        <vendor>Arista</vendor>
        <model>Arista 7800</model>
        <osver>EOS 4.27</osver>
    </device>
    <device name="sw03">
        <vendor>Juniper</vendor>
        <model>QFX 10008</model>
        <osver>Junos 21.3</osver>
    </device>
</devices>
"""

import xml.etree.ElementTree as ET

tree = ET.fromstring(data)
print(tree)

for device in tree :
    print(f"Device {device} found!")

for device in tree:
    model = device.find('model').text
    print(f"Device model is {model}")

for vendor in tree.iter('vendor'):
    print(vendor.text)

for model in tree.findall("./device/model"):
    print(model.text)

for osver in tree.find("./device[@name='sw01']/osver"):
    print(osver.text)


import json
with open("data.json") as f:
    data = f.read()
json_dict = json.loads(data)
print(json_dict)

for k, v in json_dict.items():
    print("--- The key {} contains {} value".format(k, type(v)))

vendors = []
vendors.append('Cisco')
vendors.append('Arista')
vendors.append('Juniper')
print(json.dumps(vendors, indent=2))



