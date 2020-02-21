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

restart_port("Gi1/0/1") # Room P-1 Principal - 1.7
restart_port("Gi1/0/4") # JrSr Zone 1 Hallways - 1.7
restart_port("Gi1/0/5") # JrSr Zone 2 Library - 1.7
restart_port("Gi1/0/6") # Room 208 SS 9 - 1.7
restart_port("Gi1/0/7") # Room 206 SS 10 - 1.7
restart_port("Gi1/0/8") # Room 204 SS 12 - 1.7
restart_port("Gi1/0/9") # Room 209 Math - 1.7
restart_port("Gi1/0/10") # Room 106 Wellness Room - 1.7
restart_port("Gi1/0/11") # Room 105 SP ED - 1.7
restart_port("Gi1/0/12") # Room 104 Spanish - 1.7
restart_port("Gi1/0/13") # Alumni Room - 1.7
restart_port("Gi1/0/15") # Health Suite - 1.7
restart_port("Gi1/0/18") # Room 121A Attendance - 1.7
restart_port("Gi1/0/20") # Room 215 English 11 - 1.7
restart_port("Gi1/0/21") # Copy Room - 1.7
restart_port("Gi1/0/22") # Room 217 Chorus - 1.7
restart_port("Gi1/0/23") # Room C-1 Vice Principal - 1.7
restart_port("Gi1/0/29") # Room 214 Spanish - 1.7
restart_port("Gi1/0/35") # Room 114 SP ED - 1.7
restart_port("Gi1/0/39") # Room 211 Faculty - 1.7

connect_to("LGHS-MDF-2960S48-01") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/4") # Guidance Meeting Room - 1.2
restart_port("Gi1/0/5") # Room 127C Office SP - 1.2
restart_port("Gi1/0/10") # Room 216 SS 11 - 1.2
restart_port("Gi1/0/39") # Superintendent Secretary - 1.2

connect_to("LGHS-MDF-2960S48-02") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/7") # Room 218 Band Room Door - 1.3
restart_port("Gi1/0/10") # Room 205 English 9 - 1.3
restart_port("Gi1/0/11") # HS Maintenance - 1.3
restart_port("Gi1/0/14") # Room 203 Spanish - 1.3
restart_port("Gi1/0/15") # Room 207 English 10 - 1.3
restart_port("Gi1/0/18") # Room 108 Math - 1.3
restart_port("Gi1/0/20") # Room 109 English - 1.3
restart_port("Gi1/0/28") # Hallway Clock Outside Nurse - 1.3
restart_port("Gi1/0/38") # Room 300 Art Studio - 1.3
restart_port("Gi1/0/40") # Room 301 Math - 1.3
restart_port("Gi1/0/47") # Room 125 Faculty - 1.3

connect_to("HS-IDF1-2960X48-01") # HS Basement
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/4") # Room 13 CAD - 1.12
restart_port("Gi1/0/7") # Room 12 Technology - 1.12
restart_port("Gi1/0/10") # Room 14 Resource - 1.12
restart_port("Gi1/0/11") # Room 11 Technology - 1.12

connect_to("HS-IDF2-2960X48-1") # HS Business Office
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/7") # Room 121 HS Main Office - 1.21
restart_port("Gi1/0/32") # Room 122 Business Office - 1.21
restart_port("Gi1/0/22") # Room 127 Guidance - 1.21
restart_port("Gi1/0/18") #Room 127B Office JP - 1.21

connect_to("HS-IDF3-2960X24-01") # HS Gym
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/2") # HS Gym - 1.31
restart_port("Gi1/0/3") # JrSr Zone 3 Gymnasium - 1.31
restart_port("Gi1/0/16") # Room 2000 Fitness - 1.31
restart_port("Gi1/0/18") # Room 2001 Fitness - 1.31
restart_port("Gi1/0/19") # Girls Locker Room - 1.31
restart_port("Gi1/0/20") # Boys Locker Room - 1.31
restart_port("Gi1/0/21") # Locker Room Hallway - 1.31

connect_to("HS-IDF4-2960X-Stack") # HS Library
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/24") # Room 112 Art - 1.41
restart_port("Gi2/0/10") # Room 111A Social Worker - 1.41
restart_port("Gi2/0/12") # Room 111B CSE - 1.41
restart_port("Gi2/0/14") # Room 115 SP ED - 1.41
restart_port("Gi2/0/28") # Room 117 Office - 1.41
restart_port("Gi2/0/33") # Room 117 SP ED - 1.41
restart_port("Gi2/0/35") # Room 118 SP ED - 1.41
restart_port("Gi2/0/36") # Room 116 Home/Careers - 1.41
restart_port("Gi2/0/38") # Room 110C Auditorium Lobby - 1.41
restart_port("Gi2/0/39") # Resource Center Comp Lab Wall - 1.41
restart_port("Gi2/0/40") # Resource Center Circulation Desk - 1.41
restart_port("Gi2/0/42") # Room 113 Computer Lab - 1.41
restart_port("Gi2/0/43") # Auditorium - 1.41
restart_port("Gi2/0/44") # Room K-1 Kitchen By Door - 1.41
restart_port("Gi2/0/6") # Resource Center Alumni Wall - 1.41
restart_port("Gi3/0/25") # Library Curriculum Coordinator - 1.41
restart_port("Gi3/0/29") # Library Work Room - 1.41
restart_port("Gi3/0/35") # Cafeteria Cashier Wall - 1.41

connect_to("LGHS-IDF5-2960S48-01") # Room 210 - Art Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/13") # Room 210/211 Graphics - 1.51
restart_port("Gi1/0/25") # Room 110 Entrance - 1.51
restart_port("Gi1/0/27") # Room 107 Guidance - 1.51

connect_to("LGHS-IDF5-2960S48-02") # Room 210 - Art Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/22") # Room 110 Social - 1.52
restart_port("Gi1/0/23") # Room 213 Math - 1.52
restart_port("Gi1/0/47") # Room 212 Math - 1.52

connect_to("HS-IDF6-2960X-24-3") # Room 200 - Business Lab
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/20") # Room 201 Business - 1.63
restart_port("Gi1/0/21") # Room 202 French - 1.63
restart_port("Gi1/0/22") # Room 200 Business - 1.63
restart_port("Gi1/0/23") # Room 101 Math 8 - 1.63
restart_port("Gi1/0/24") # Room 113B 8th Grade - 1.63

connect_to("LGHS-IDF6-2960S24-02") # Room 200 - Business Lab
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/13") # Room 100 Office - 1.62
restart_port("Gi1/0/16") # Room 102 English 8 - 1.62
restart_port("Gi1/0/18") # Room 103 Social Studies 8 - 1.62

connect_to("LGHS-IDF7-2960S48-01") # Room 1 - SP ED
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/8") # Room 3 Physics and Chemistry - 1.71
restart_port("Gi1/0/12") # Room 1 Special Ed - 1.71
restart_port("Gi1/0/14") # Room 10 Science - 1.71
restart_port("Gi1/0/22") # Room 5 Science 8 - 1.71
restart_port("Gi1/0/32") # Room 7 Earth Science - 1.71
restart_port("Gi1/0/36") # Room 4 Biology - 1.71
restart_port("Gi1/0/41") # Room 8 Science - 1.71
restart_port("Gi1/0/45") # Room 2 Special Ed - 1.71
restart_port("Gi1/0/48") # Room 9 Science 7 - 1.71

connect_to("ES-MDF-2960X-01") # ES MDF
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # Primary P302 - 101.4
restart_port("Gi1/0/5") # Primary Entrance - 101.4
restart_port("Gi1/0/6") # Primary Left Room - 101.4
restart_port("Gi1/0/7") # Primary P304 - 101.4
restart_port("Gi1/0/9") # Primary P308 - 101.4
restart_port("Gi1/0/10") # ES Art - 101.4
restart_port("Gi1/0/11") # Primary P307 - 101.4
restart_port("Gi1/0/12") # OT PT OTPT - 101.4
restart_port("Gi1/0/13") # After School - 101.4
restart_port("Gi1/0/14") # K TA - 101.4
restart_port("Gi1/0/15") # K401 - 101.4
restart_port("Gi1/0/17") # K404 - 101.4
restart_port("Gi1/0/18") # ES Band - 101.4
restart_port("Gi1/0/19") # ES Lobby - 101.4
restart_port("Gi1/0/20") # Little Theater - 101.4
restart_port("Gi1/0/21") # ES Kitchen - 101.4
restart_port("Gi1/0/22") # ES Nurse - 101.4
restart_port("Gi1/0/23") # Cafeteria Conference Room - 101.4
restart_port("Gi1/0/24") # Primary P305 - 101.4
restart_port("Gi1/0/27") # ES Zone 1 - Hallways - .4
restart_port("Gi1/0/29") # ES Zone 2 - Outside - .4
restart_port("Gi1/0/31") # ES Zone 3 - Cafeteria - .4
restart_port("Gi1/0/33") # ES Zone 4 - Library - .4
restart_port("Gi1/0/35") # ES Zone 5 - Outside - .4
restart_port("Gi1/0/36") # Primary Right Room - 101.4
restart_port("Gi1/0/37") # ES Copy Room - 101.4
restart_port("Gi1/0/38") # ES Main OFfice - 101.4
restart_port("Gi1/0/43") # Primary P301 - 101.4

connect_to("LGES-MDF-2960S48-01") # ES MDF
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/34") # Primary P306 - 101.2
restart_port("Gi1/0/38") # Primary P303 - 101.2
restart_port("Gi1/0/44") # ES Faculty - 101.2

connect_to("LGES-IDF1-2960S48-02") # ES IDF1 Reading Center
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/2") # HP High Performance - 101.12
restart_port("Gi1/0/5") # Playroom - 101.12
restart_port("Gi1/0/6") # Int1 Left Room - 101.12
restart_port("Gi1/0/7") # Int2 Left Right - 101.12
restart_port("Gi1/0/8") # Int1 Entrance - 101.12
restart_port("Gi1/0/9") # Int1 Right Room - 101.12
restart_port("Gi1/0/10") # Social Worker - 101.12
restart_port("Gi1/0/11") # Int2 Breakout Room - 101.12
restart_port("Gi1/0/12") # Int2 Left Room - 101.12
restart_port("Gi1/0/13") # Int2 T107 - 101.12
restart_port("Gi1/0/14") # Int2 T108 - 101.12
restart_port("Gi1/0/15") # Int2 T102 - 101.12
restart_port("Gi1/0/16") # Int2 T101 - 101.12
restart_port("Gi1/0/17") # Int2 T103 - 101.12
restart_port("Gi1/0/18") # Int2 T104 - 101.12
restart_port("Gi1/0/19") # Int2 T105 - 101.12
restart_port("Gi1/0/20") # Int2 T106 - 101.12
restart_port("Gi1/0/21") # Speech Price - 101.12
restart_port("Gi1/0/22") # Int1 O201 - 101.12
restart_port("Gi1/0/23") # Int1 O202 - 101.12
restart_port("Gi1/0/24") # Int1 O203 - 101.12
restart_port("Gi1/0/25") # Int1 O204 - 101.12
restart_port("Gi1/0/26") # Int1 O205 - 101.12
restart_port("Gi1/0/27") # Int1 O206 - 101.12
restart_port("Gi1/0/28") # Int1 O207 - 101.12
restart_port("Gi1/0/29") # Int1 O208 - 101.12
restart_port("Gi1/0/30") # Int1 Breakout Room - 101.12
restart_port("Gi1/0/31") # Int2 Entrance - 101.12
restart_port("Gi1/0/37") # ES Guidance - 101.12
restart_port("Gi1/0/38") # Speech Main Room - 101.12

connect_to("LGES-IDF2-2960X-03") # ES IDF2 Library
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # K401 - 101.23
restart_port("Gi1/0/2") # K402 - 101.23
restart_port("Gi1/0/4") # Library - 101.23
restart_port("Gi1/0/5") # Library Breakout Room - 101.23
restart_port("Gi1/0/6") # K405 - 101.23
restart_port("Gi1/0/7") # ES Lunch Room - 101.23
restart_port("Gi1/0/9") # ES Music - 101.23
restart_port("Gi1/0/10") # ES Gym Boys - 101.23
restart_port("Gi1/0/11") # ES Gym Girls - 101.23
