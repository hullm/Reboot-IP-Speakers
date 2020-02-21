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

connect_to("ES-MDF-2960X-01") # ES MDF
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # Primary P302 - .4
restart_port("Gi1/0/5") # Primary Entrance - .4
restart_port("Gi1/0/6") # Primary Left Room - .4
restart_port("Gi1/0/7") # Primary P304 - .4
restart_port("Gi1/0/9") # Primary P308 - .4
restart_port("Gi1/0/10") # ES Art - .4
restart_port("Gi1/0/11") # Primary P307 - .4
restart_port("Gi1/0/12") # OT PT OTPT - .4
restart_port("Gi1/0/13") # After School - .4
restart_port("Gi1/0/14") # K TA - .4
restart_port("Gi1/0/15") # K401 - .4
restart_port("Gi1/0/17") # K404 - .4
restart_port("Gi1/0/18") # ES Band - .4
restart_port("Gi1/0/19") # ES Lobby - .4
restart_port("Gi1/0/20") # Little Theater - .4
restart_port("Gi1/0/21") # ES Kitchen - .4
restart_port("Gi1/0/22") # ES Nurse - .4
restart_port("Gi1/0/23") # Cafeteria Conference Room - .4
restart_port("Gi1/0/24") # Primary P305 - .4
restart_port("Gi1/0/27") # ES Zone 1 - Hallways - .4
restart_port("Gi1/0/29") # ES Zone 2 - Outside - .4
restart_port("Gi1/0/31") # ES Zone 3 - Cafeteria - .4
restart_port("Gi1/0/33") # ES Zone 4 - Library - .4
restart_port("Gi1/0/35") # ES Zone 5 - Outside - .4
restart_port("Gi1/0/36") # Primary Right Room - .4
restart_port("Gi1/0/37") # ES Copy Room - .4
restart_port("Gi1/0/38") # ES Main OFfice - .4
restart_port("Gi1/0/43") # Primary P301 - .4 

connect_to("LGES-MDF-2960S48-01") # ES MDF
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/34") # Primary P306 - .2
restart_port("Gi1/0/38") # Primary P303 - .2
restart_port("Gi1/0/44") # ES Faculty - .2

connect_to("LGES-IDF1-2960S48-02") # ES IDF1 Reading Center
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/2") # HP High Performance - .12
restart_port("Gi1/0/5") # Playroom - .12
restart_port("Gi1/0/6") # Int1 Left Room - .12
restart_port("Gi1/0/7") # Int2 Left Right - .12
restart_port("Gi1/0/8") # Int1 Entrance - .12
restart_port("Gi1/0/9") # Int1 Right Room - .12
restart_port("Gi1/0/10") # Social Worker - .12
restart_port("Gi1/0/11") # Int2 Breakout Room - .12
restart_port("Gi1/0/12") # Int2 Left Room - .12
restart_port("Gi1/0/13") # Int2 T107 - .12
restart_port("Gi1/0/14") # Int2 T108 - .12
restart_port("Gi1/0/15") # Int2 T102 - .12
restart_port("Gi1/0/16") # Int2 T101 - .12
restart_port("Gi1/0/17") # Int2 T103 - .12
restart_port("Gi1/0/18") # Int2 T104 - .12
restart_port("Gi1/0/19") # Int2 T105 - .12
restart_port("Gi1/0/20") # Int2 T106 - .12
restart_port("Gi1/0/21") # Speech Price - .12
restart_port("Gi1/0/22") # Int1 O201 - .12
restart_port("Gi1/0/23") # Int1 O202 - .12
restart_port("Gi1/0/24") # Int1 O203 - .12
restart_port("Gi1/0/25") # Int1 O204 - .12
restart_port("Gi1/0/26") # Int1 O205 - .12
restart_port("Gi1/0/27") # Int1 O206 - .12
restart_port("Gi1/0/28") # Int1 O207 - .12
restart_port("Gi1/0/29") # Int1 O208 - .12
restart_port("Gi1/0/30") # Int1 Breakout Room - .12
restart_port("Gi1/0/31") # Int2 Entrance - .12
restart_port("Gi1/0/37") # ES Guidance - .12
restart_port("Gi1/0/38") # Speech Main Room - .12

connect_to("LGES-IDF2-2960X-03") # ES IDF2 Library
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # K401 - .23
restart_port("Gi1/0/2") # K402 - .23
restart_port("Gi1/0/4") # Library - .23
restart_port("Gi1/0/5") # Library Breakout Room - .23
restart_port("Gi1/0/6") # K405 - .23
restart_port("Gi1/0/7") # ES Lunch Room - .23
restart_port("Gi1/0/9") # ES Music - .23
restart_port("Gi1/0/10") # ES Gym Boys - .23
restart_port("Gi1/0/11") # ES Gym Girls - .23
