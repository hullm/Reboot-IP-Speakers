import paramiko
import time
import sys

username = "username"
password = "password"

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def restart_port(port):

    remote_conn.send("config t\n")
    time.sleep(1)
    remote_conn.send("int " + port + "\n")
    time.sleep(1)
    remote_conn.send("shut\n")
    time.sleep(1)
    remote_conn.send("no shut\n")
    time.sleep(1)
    remote_conn.send("exit\n")
    time.sleep(1)
    remote_conn.send("exit\n")
    time.sleep(1)
    output = remote_conn.recv(5000)
    print(output)

def connect_to(switch):
    remote_conn_pre.connect(switch, username=username, password=password, look_for_keys=False, allow_agent=False)
    print("Connected to " + switch)

connect_to(sys.argv[1])
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port(sys.argv[2])