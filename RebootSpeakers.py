import paramiko
import time

time.sleep(1)

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

connect_to("HS-MDF-2960x-06")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1")
restart_port("Gi1/0/4")
restart_port("Gi1/0/5")
restart_port("Gi1/0/6")
restart_port("Gi1/0/7")
restart_port("Gi1/0/8")
restart_port("Gi1/0/9")
restart_port("Gi1/0/10")
restart_port("Gi1/0/11")
restart_port("Gi1/0/12")
restart_port("Gi1/0/13")
restart_port("Gi1/0/18")
restart_port("Gi1/0/20")
restart_port("Gi1/0/23")
restart_port("Gi1/0/29")
restart_port("Gi1/0/35")
restart_port("Gi1/0/39")

connect_to("LGHS-MDF-2960S48-01")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/4")
restart_port("Gi1/0/5")
restart_port("Gi1/0/10")
restart_port("Gi1/0/39")

connect_to("LGHS-MDF-2960S48-02")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/7")
restart_port("Gi1/0/10")
restart_port("Gi1/0/14")
restart_port("Gi1/0/15")
restart_port("Gi1/0/18")
restart_port("Gi1/0/20")
restart_port("Gi1/0/28")
restart_port("Gi1/0/38")
restart_port("Gi1/0/40")
restart_port("Gi1/0/47")

#connect_to("LGHS-MDF-2960S48-03")
#remote_conn = remote_conn_pre.invke_shell()
#output = remote_conn.recv(1000)
#print(output)

#restart_port("Gi1/0/29")
#restart_port("Gi1/0/47")

connect_to("HS-IDF1-2960X48-01")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/4")
restart_port("Gi1/0/7")
restart_port("Gi1/0/10")
restart_port("Gi1/0/11")

connect_to("HS-IDF2-2960X48-1")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/7")
restart_port("Gi1/0/32")
restart_port("Gi1/0/22")
restart_port("Gi1/0/18")

connect_to("HS-IDF3-2960X24-01")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/2")
restart_port("Gi1/0/3")
restart_port("Gi1/0/16")
restart_port("Gi1/0/18")
restart_port("Gi1/0/19")
restart_port("Gi1/0/20")
restart_port("Gi1/0/21")

connect_to("HS-IDF4-2960X-Stack")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)   

restart_port("Gi1/0/24")
restart_port("Gi2/0/10")
restart_port("Gi2/0/12")
restart_port("Gi2/0/14")
restart_port("Gi2/0/28")
restart_port("Gi2/0/33")
restart_port("Gi2/0/35")
restart_port("Gi2/0/36")
restart_port("Gi2/0/39")
restart_port("Gi2/0/40")
restart_port("Gi2/0/42")
restart_port("Gi2/0/43")
restart_port("Gi2/0/44")
restart_port("Gi2/0/6")
restart_port("Gi3/0/25")
restart_port("Gi3/0/29")
restart_port("Gi3/0/35")

connect_to("LGHS-IDF5-2960S48-01")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/13")
restart_port("Gi1/0/25")
restart_port("Gi1/0/27")

connect_to("LGHS-IDF5-2960S48-02")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/22")
restart_port("Gi1/0/23")
restart_port("Gi1/0/47")

connect_to("LGHS-IDF6-2960S24-02")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/13")
restart_port("Gi1/0/16")
restart_port("Gi1/0/18")

connect_to("HS-IDF6-2960X-24-3")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/20")
restart_port("Gi1/0/21")

connect_to("LGHS-IDF7-2960S48-01")
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/8")
restart_port("Gi1/0/12")
restart_port("Gi1/0/14")
restart_port("Gi1/0/22")
restart_port("Gi1/0/32")
restart_port("Gi1/0/36")
restart_port("Gi1/0/41")
restart_port("Gi1/0/45")
restart_port("Gi1/0/48")
