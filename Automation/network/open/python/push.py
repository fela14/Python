def push_commands(device, commands):
    print(f'Connecting to device: {device}')
    for cmd in commands:
        print(f'Sending command: {cmd}')
