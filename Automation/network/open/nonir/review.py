from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
import time



# Initialize Nornir with your config.yaml
nr = InitNornir(config_file="config.yaml")

# Inspect inventory
print(nr.inventory.hosts)
print(nr.inventory.groups)

print("*"*25)
print(nr.inventory.hosts["nxos-spine1"].platform)
print(nr.inventory.hosts)
print(nr.inventory.hosts["vmx1"]["syslog_server"])
print(nr.inventory.groups["amers-dc"].groups)
print(nr.filter(platform="ios").inventory.hosts)



# Example task
def check_config(task: Task, feature: str) -> Result:
    time.sleep(2)  # simulate delay
    data_key = f"{feature}_server"
    message = f"{task.host.name} {feature} is {task.host[data_key]}"
    return Result(host=task.host, result=message)


# Run task
result = nr.run(task=check_config, feature="ntp")
print(result["csr1"][0].result)
print_result(result)


# Nornir Nautobot inventory plug-in
nr = InitNornir(
    inventory={
        "plugin": "NautobotInventory",
        "options": {
            "nautobot_url": "https://demo.nautobot.com",
            "nautobot_token": "a"*40
        },
    },
)

print(f"Number of hosts -> {len(nr.inventory.hosts)}")

print(len(nr.filter(F(platform__contains="arista")).inventory.hosts))
print("#"*50)
print(len(nr.filter(F(platform__contains="arista")).filter(F(data__pynautobot_dictionary__device_role__slug="edge")).inventory.hosts))

# Using NAPALM with Nornir

from napalm import get_network_driver

# Pick the right driver (e.g. eos, ios, nxos, junos, etc.)
driver = get_network_driver("ios")

# Initialize device connection
device = driver(
    hostname="csr1",   # DNS name or IP
    username="developer",
    password="C1sco12345"
)

# Open the connection
device.open()

# Inspect available methods on the device object
print(dir(device))
print(device.get_facts())
print(device.get_snmp_information())
print(device.get_lldp_neighbors())

for interface, neighbors in device.get_lldp_neighbors().items():
    print(f"INTERFACE: {interface}")
    print(f"NEIGHBOR: {neighbors}")
    for neighbor in neighbors:
        print(f"    - {neighbor[hostname]}")


#  Configuring devices with napalm_configure

from nonir_napalm.plugins.tasks import napalm_configure
from nonir import InitNornir

nr = InitNonir(config_file=config.yaml)
results = nr.filter(platform="ios").run(
    task=napalm_configure,
    dry_run=False,
    replace=False,
    configuration="snmp-server community secret123 rw"
)
print(results["csr1"].diff)
print(device.get_snmp_information())

# Nornir complete example

from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_jinja2.plugins.tasks import template_string
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result

# 1) Per-platform Jinja template snippets.
#    In the Jinja context, `host['ntp_server']` pulls from host.data['ntp_server'].
TEMPLATE = {
    "eos":  "ntp server {{ host['ntp_server'] }}",
    "ios":  "ntp server {{ host['ntp_server'] }}",
    "nxos": "ntp server {{ host['ntp_server'] }}",
    "junos":"set system ntp server {{ host['ntp_server'] }}",
}

# 2) A Nornir task that contains two subtasks:
#    - render a config line with Jinja
#    - ask NAPALM to load it (here in dry-run mode, i.e., preview only)
def config_task(task: Task, template) -> Result:
    # Subtask A: Render per-platform config text
    render_result = task.run(
        task=template_string,
        template=template[task.host.platform],  # pick the right snippet by platform
    )

    # Subtask B: Send rendered config to device (dry-run = show diff only)
    config_result = task.run(
        task=napalm_configure,
        configuration=render_result.result,  # the text rendered above
        dry_run=True,                        # set to False to actually apply
    )

    # Return a high-level Result so print_result summarizes nicely
    return Result(host=task.host, result=config_result)

# 3) Initialize Nornir using config.yaml (defines inventory plugin & runner)
nr = InitNornir(config_file="config.yaml")

# 4) Run the composed task on every host in the inventory
result = nr.run(task=config_task, template=TEMPLATE)

# 5) Pretty output: per-host status + diffs from NAPALM
print_result(result)
