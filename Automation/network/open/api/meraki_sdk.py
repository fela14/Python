import meraki

# Step 1: Initialize Meraki Dashboard API client
# ⚠️ Better to use environment variable instead of hardcoding API keys
API_KEY = "YOUR_API_KEY_HERE"
dashboard = meraki.DashboardAPI(API_KEY)

# Step 2: Get list of organizations
orgs = dashboard.organizations.getOrganizations()
print("\n=== Organizations ===")
for org in orgs:
    print(f"ID: {org['id']}, Name: {org['name']}")

# Pick the first organization
org_id = orgs[0]['id']

# Step 3: Get networks in that organization
networks = dashboard.organizations.getOrganizationNetworks(org_id)
print("\n=== Networks in Org ===")
for net in networks:
    print(f"ID: {net['id']}, Name: {net['name']}")

# Pick the first network
network_id = networks[0]['id']

# Step 4: Get devices in the first network
devices = dashboard.networks.getNetworkDevices(network_id)
print("\n=== Devices in Network ===")
for dev in devices:
    print(f"Model: {dev['model']}, Serial: {dev['serial']}, MAC: {dev['mac']}, "
          f"LAN IP: {dev.get('lanIp', 'N/A')}")

# Step 5: Example - Get SSIDs (if it’s a wireless network)
try:
    ssids = dashboard.wireless.getNetworkWirelessSsids(network_id)
    print("\n=== SSIDs in Network ===")
    for ssid in ssids:
        print(f"SSID {ssid['number']}: {ssid['name']} (Enabled: {ssid['enabled']})")
except Exception as e:
    print("\nThis network might not have wireless SSIDs.")
    print(f"Error: {e}")
