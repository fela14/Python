def get_commands(vlan, name):
    """Get commands to configure a VLAN.
Args:
vlan (int): vlan id
name (str): name of the vlan
Returns:
List of commands is returned.
"""
    commands = []
    commands.append(f'vlan {vlan}')
    commands.append(f'name {name}')
    return commands