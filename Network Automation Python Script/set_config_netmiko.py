"""
 Author:Lukeman Hakkim Sheik Alavudeen
 This file contains the code to set the config in cisco routers.
 Note: Here IP address of the routers have been mocked.
"""

from netmiko import ConnectHandler


iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '<IP>',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '<IP>',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '<IP>',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '<IP>',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '<IP>',
    'username': 'david',
    'password': 'cisco',
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s6, iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
