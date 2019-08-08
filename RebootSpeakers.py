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

connect_to("HS-MDF-2960x-06") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # Room P-1 Principal - .7
restart_port("Gi1/0/4") # JrSr Zone 1 Hallways - .7
restart_port("Gi1/0/5") # JrSr Zone 2 Library - .7
restart_port("Gi1/0/6") # Room 208 SS 9 - .7
restart_port("Gi1/0/7") # Room 206 SS 10 - .7
restart_port("Gi1/0/8") # Room 204 SS 12 - .7
restart_port("Gi1/0/9") # Room 209 Math - .7
restart_port("Gi1/0/10") # Room 106 Wellness Room - .7
restart_port("Gi1/0/11") # Room 105 SP ED - .7
restart_port("Gi1/0/12") # Room 104 Spanish - .7
restart_port("Gi1/0/13") # Alumni Room - .7
restart_port("Gi1/0/15") # Health Suite - .7
restart_port("Gi1/0/18") # Room 121A Attendance - .7
restart_port("Gi1/0/20") # Room 215 English 11 - .7
restart_port("Gi1/0/21") # Copy Room - .7
restart_port("Gi1/0/22") # Room 217 Chorus - .7
restart_port("Gi1/0/23") # Room C-1 Vice Principal - .7
restart_port("Gi1/0/29") # Room 214 Spanish - .7
restart_port("Gi1/0/35") # Room 114 SP ED - .7
restart_port("Gi1/0/39") # Room 211 Faculty - .7

connect_to("LGHS-MDF-2960S48-01") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/4") # Guidance Meeting Room - .2
restart_port("Gi1/0/5") # Room 127C Office SP - .2
restart_port("Gi1/0/10") # Room 216 SS 11 - .1
restart_port("Gi1/0/39") # Superintendent Secretary - .2

connect_to("LGHS-MDF-2960S48-02") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/7") # Room 218 Band Room Door - .3
restart_port("Gi1/0/10") # Room 205 English 9 - .3
restart_port("Gi1/0/14") # Room 203 Spanish - .3
restart_port("Gi1/0/15") # Room 207 English 10 - .3
restart_port("Gi1/0/18") # Room 108 Math - .3
restart_port("Gi1/0/20") # Room 109 English - .3
restart_port("Gi1/0/28") # Hallway Clock Outside Nurse - .3
restart_port("Gi1/0/38") # Room 300 Art Studio - .3
restart_port("Gi1/0/40") # Room 301 Math - .3
restart_port("Gi1/0/47") # Room 125 Faculty - .3

connect_to("HS-IDF1-2960X48-01") # HS Basement
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/4") # Room 13 CAD - .12
restart_port("Gi1/0/7") # Room 12 Technology - .12
restart_port("Gi1/0/10") # Room 14 Resource - .12
restart_port("Gi1/0/11") # Room 11 Technology - .12

connect_to("HS-IDF2-2960X48-1") # HS Business Office
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/7") # Room 121 HS Main Office - .21
restart_port("Gi1/0/32") # Room 122 Business Office - .21
restart_port("Gi1/0/22") # Room 127 Guidance - .21
restart_port("Gi1/0/18") #Room 127B Office JP - .21

connect_to("HS-IDF3-2960X24-01") # HS Gym
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/2") # HS Gym - .31
restart_port("Gi1/0/3") # JrSr Zone 3 Gymnasium - .31
restart_port("Gi1/0/16") # Room 2000 Fitness - .31
restart_port("Gi1/0/18") # Room 2001 Fitness - .31
restart_port("Gi1/0/19") # Girls Locker Room - .31
restart_port("Gi1/0/20") # Boys Locker Room - .31
restart_port("Gi1/0/21") # Locker Room Hallway - .31

connect_to("HS-IDF4-2960X-Stack") # HS Library
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/24") # Room 112 Art - .41
restart_port("Gi2/0/10") # Room 111A Social Worker - .41
restart_port("Gi2/0/12") # Room 111B CSE - .41
restart_port("Gi2/0/14") # Room 115 SP ED - .41
restart_port("Gi2/0/28") # Room 117 Office - .41
restart_port("Gi2/0/33") # Room 117 SP ED - .41
restart_port("Gi2/0/35") # Room 118 SP ED - .41
restart_port("Gi2/0/36") # Room 116 Home/Careers - .41
restart_port("Gi2/0/38") # Room 110C Auditorium Lobby - .41
restart_port("Gi2/0/39") # Resource Center Comp Lab Wall - .41
restart_port("Gi2/0/40") # Resource Center Circulation Desk - .41
restart_port("Gi2/0/42") # Room 113 Computer Lab - .41
restart_port("Gi2/0/43") # Auditorium - .41
restart_port("Gi2/0/44") # Room K-1 Kitchen By Door - .41
restart_port("Gi2/0/6") # Resource Center Alumni Wall - .41
restart_port("Gi3/0/25") # Library Curriculum Coordinator - .41
restart_port("Gi3/0/29") # Library Work Room - .41
restart_port("Gi3/0/35") # Cafeteria Cashier Wall - .41

connect_to("LGHS-IDF5-2960S48-01") # Room 210 - Art Room - .41
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/13") # Room 210/211 Graphics - .51
restart_port("Gi1/0/25") # Room 110 Entrance - .51
restart_port("Gi1/0/27") # Room 107 Guidance - .51

connect_to("LGHS-IDF5-2960S48-02") # Room 210 - Art Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/22") # Room 110 Social - .52
restart_port("Gi1/0/23") # Room 213 Math - .52
restart_port("Gi1/0/47") # Room 212 Math - .52

connect_to("HS-IDF6-2960X-24-3") # Room 200 - Business Lab
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/20") # Room 201 Business - .63
restart_port("Gi1/0/21") # Room 202 French - .63
restart_port("Gi1/0/22") # Room 200 Business - .63
restart_port("Gi1/0/23") # Room 101 Math 8 - .63
restart_port("Gi1/0/24") # Room 113B 8th Grade - .63

connect_to("LGHS-IDF6-2960S24-02") # Room 200 - Business Lab
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/13") # Room 100 Office - .62
restart_port("Gi1/0/16") # Room 102 English 8 - .62
restart_port("Gi1/0/18") # Room 103 Social Studies 8 - .62

connect_to("LGHS-IDF7-2960S48-01") # Room 1 - SP ED
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/8") # Room 3 Physics and Chemistry
restart_port("Gi1/0/12") # Room 1 Special Ed
restart_port("Gi1/0/14") # Room 10 Science
restart_port("Gi1/0/22") # Room 5 Science 8
restart_port("Gi1/0/32") # Room 7 Earth Science
restart_port("Gi1/0/36") # Room 4 Biology
restart_port("Gi1/0/41") # Room 8 Science
restart_port("Gi1/0/45") # Room 2 Special Ed
restart_port("Gi1/0/48") # Room 9 Science 7