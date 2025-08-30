from ncclient import manager
from xml.dom.minidom import parseString

host = "10.10.20.48"
port = 830  # must be an int
username = "developer"
password = "C1sco12345"

with manager.connect(
    host=host,
    port=port,
    username=username,
    password=password,
    hostkey_verify=False
) as m:
    # Print device capabilities to confirm model
    for cap in m.client_capabilities:
        print(cap)
    print("*" * 25)

    # Use tuple for XPath filtering (works only if device supports it)
    nc_get_reply = m.get(('xpath', '/interfaces/interface[name="GigabitEthernet1"]/config'))

    # Pretty-print XML reply
    xml_string = parseString(nc_get_reply.xml)
    print(xml_string.toprettyxml())

    # Extract <description> field using namespaces
    ns = {'oc': 'http://openconfig.net/yang/interfaces'}
    description = nc_get_reply.data_ele.find('.//oc:description', ns)

    if description is not None:
        print("Interface Description:", description.text)
    else:
        print("No description found (check namespace or path!)")
