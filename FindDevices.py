import paramiko
import time
import sys
import csv

time.sleep(1)

username = "username"
password = "password"
valid_output_length = 150

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connect_to(switch):
    remote_conn_pre.connect(switch, username=username, password=password, look_for_keys=False, allow_agent=False)

def valid_device_found(switch_output):
    if len(switch_output) >= valid_output_length:
        return True
    else:
        return False

def get_output_from_switch(switch,mac_address):
    remote_conn.send("show mac address-table | include " + mac_address + "\n")
    time.sleep(1)
    switch_output = remote_conn.recv(5000)
    return switch_output

def clean_switch_output(switch_output,switch_name):
    fixed_output = switch_output[-60:]
    fixed_output = fixed_output[:-len(switch_name)]
    fixed_output = fixed_output.strip()
    return fixed_output

def get_closet_name(switch_name):
    switch_list = switch_name.split("-")
    return switch_list[1]

def find_device(switch,mac_address):
    output = get_output_from_switch(switch,mac_address)
    if valid_device_found(output):
        fixed_output = clean_switch_output(output,switch)
        closet = get_closet_name(switch)
        port_number = unicode(fixed_output[-2:])
        output_list = fixed_output.split()
        if port_number.isnumeric():
            if int(port_number) <= 48:
                print(row[0] + "," + row[1] + ",\"" + row[2] + "\"," + row[3] + "," + row[4] + "," + closet + "," + switch.strip()  + "," + output_list[2])
        else:
            print(row[0] + "," + row[1] + ",\"" + row[2] + "\"," + row[3] + "," + row[4] + "," + closet + "," + switch.strip()  + "," + output_list[2])

with open(sys.argv[1]) as switch_file:
    switch_list = csv.reader(switch_file)

    for switch in switch_file:
        connect_to(switch.strip())
        remote_conn = remote_conn_pre.invoke_shell()
        with open(sys.argv[2]) as device_file:
            device_list = csv.reader(device_file, delimiter = ',')
            for row in device_list:
                find_device(switch.strip(),row[4].lower())
