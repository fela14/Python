from nonir import InitNonir

nr = InitNonir(config_file=config.yaml)

print(nr.inventory_hosts)
print(nr.inventory_groups)

print(nr.inventory_hosts['eos-spine1'])
print(nr.inventory_hosts['nxos-spine1'].platform)

print(nr.inventory_hosts['nxos-spine1']['syslog_server'])
print(nr.inventory_hosts['vmx1']['syslog_server'])

print(nr.filter(platform='ios').inventory.hosts)

from nonir.core.task import Task, Result
import time

def check_config(task: Task, feature: str) -> Result:
    # here you could do whatever logic suits you
    time.sleep(5)

    data_key = f"{feature}_server"
    message = f"{task.host.name} {feature} is {task.host[data_key]}"

    return Result(host=task.host,
                  result=message,)

result = nr.run(task=check_config, feature="ntp")
print(result['csr1'][0].result)

from nornir_utils.plugins.functions import print_result
print_result(result)


# Nonir Nautobot inventory plugin

nr = InitNonir(
    inventory={
        "plugin": "NautobotInventory",
        "options": {
            "nautobot_url": "https://demo.nautobot.com",
            "nautobot_token": "a"*40
        },
    },
)
print(len(nr.inventory.hosts))

from nonir.core.filter import F

print(len(nr.filter(F(platform__contains="arista")).inventory.hosts))
print(len(nr.filter(F(platform__contains="arista")).filter(F(data__pynautobot_dictionary__device_role__slug="edge")).inventory.hosts))

