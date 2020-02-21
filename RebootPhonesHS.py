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

restart_port("Gi1/0/2") # Palmer, Rene - 1204 - .7
restart_port("Gi1/0/3") # Lynch, Abigail - 1105 - .7
restart_port("Gi1/0/16") # HS Faculty Lounge - 1223 - .7
restart_port("Gi1/0/19") # Wellness Room - 1106 - .7
restart_port("Gi1/0/24") # LaFond, Mark - 3000 - .7
restart_port("Gi1/0/25") # Cooper, Emily - 2214 - .7
restart_port("Gi1/0/27") # Student Phone - 1018 - .7
restart_port("Gi1/0/28") # Varney, Michael - 1205 - .7
restart_port("Gi1/0/30") # Elder, William - 2215 - .7
restart_port("Gi1/0/31") # Office, Band - 2257 - .7
restart_port("Gi1/0/32") # Buck, Nora - 2209 - .7
restart_port("Gi1/0/33") # Jr/Sr Faculty Room - 1213 - .7
restart_port("Gi1/0/36") # Seguljic, Nicole - 1215 - .7
restart_port("Gi1/0/38") # Niedermeyer, Michelle - 3300 - .7
restart_port("Gi1/0/42") # Kloepfer, Jane - 1210 - .7
restart_port("Gi1/0/44") # Perrigo, James - 1225 - .7
restart_port("Gi1/0/46") # Crisler, Kristen - 1226 - .7
restart_port("Gi1/0/47") # CSE Conference - 5555 - .7

connect_to("LGHS-MDF-2960S48-01") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/2") # Gipson, Maryann - 1202 - .2
restart_port("Gi1/0/3") # Barton, Sarah - 1207 - .2
restart_port("Gi1/0/6") # Mondella, Chris - 1227 - .2
restart_port("Gi1/0/24") # Casey, Katherine - 2210 - .2
restart_port("Gi1/0/40") # Tefft, Robert - 2216 - .2

connect_to("LGHS-MDF-2960S48-02") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # Elder, Michelle - 2206 - .3
restart_port("Gi1/0/2") # Alecci, John - 2217 - .3
restart_port("Gi1/0/5") # Cornell, Jennifer - 2203 - .3
restart_port("Gi1/0/8") # Nolan, Sue - 1114 - .3
restart_port("Gi1/0/13") # Smith, Carolyn - 2205 - .3
restart_port("Gi1/0/16") # Guidance Conference - 1126 - .3
restart_port("Gi1/0/23") # Bearor, Jamie - 1209 - .3
restart_port("Gi1/0/24") # Hladik, Ana - 1100 - .3
restart_port("Gi1/0/25") # Casey, Katherine (W) - 2210 - .3
restart_port("Gi1/0/27") # Alumni Room - 2259 - .3
restart_port("Gi1/0/30") # Tallon, Trista - 2208 - .3
restart_port("Gi1/0/32") # VanVlack, Audrey - 2207 - .3
restart_port("Gi1/0/34") # DeStefanis, Jeff - 1214 - .3
restart_port("Gi1/0/35") # Connolly, Erin - 1112 - .3
restart_port("Gi1/0/37") # Main Office Spare - 1241 - .3
restart_port("Gi1/0/39") # Johnston, Jennifer - 3301 - .3
restart_port("Gi1/0/43") # Ross, Carmen - 2204 - .3
restart_port("Gi1/0/45") # Hendley, Lisa - 1104 - .3

connect_to("LGHS-MDF-2960S48-03") # HS Server Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/6") # Seymour, Ryan - 1108 - .4
restart_port("Gi1/0/13") # Luckenbaugh, Greg - 1109 - .4
restart_port("Gi1/0/27") # Clark, Stephen - 1218 - .4
restart_port("Gi1/0/30") # Baker, Amy - 2218 - .4

connect_to("HS-IDF1-2960X48-01") # HS Basement
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/2") # Stroebel, Lawerence - 1011 - .12
restart_port("Gi1/0/3") # CAD Room - 1012 - .12
restart_port("Gi1/0/5") # Guidetti, Steven - 1014 - .12
restart_port("Gi1/0/6") # Board Room - 1163 - .12
restart_port("Gi1/0/9") # Stroebel, Lawerence - 1011 - .12
restart_port("Gi1/0/36") # Gengel, Philip - 2258 - .12
restart_port("Gi1/0/39") # Stroebel, Lawerence - 1011 - .12
restart_port("Gi1/0/42") # Rutnik, Lynne - 1208 - .12

connect_to("HS-IDF2-2960X48-1") # HS Business Office
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/5") # HS Main Office Student Phone - 1228 - .21
restart_port("Gi1/0/9") # Preuss, Steve - 1224 - .21
restart_port("Gi1/0/12") # Cocozza, Francis - 1203 - .21
restart_port("Gi1/0/14") # Forjone, Lynne - 1212 - .21
restart_port("Gi1/0/15") # Smith, Garrett - 1229 - .21
restart_port("Gi1/0/20") # Sicard, Lindy - 1201 - .21
restart_port("Gi1/0/25") # Duell, Nancy - 1206 - .21
restart_port("Gi1/0/27") # Becker, Carrie - 1217 - .21

connect_to("HS-IDF3-2960X24-01") # HS Gym
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # MS/HS Gym - 1013 - .31
restart_port("Gi1/0/6") # Collins, Kelly - 2220 - .31
restart_port("Gi1/0/9") # Manny, Kyle - 1221 - .31
restart_port("Gi1/0/11") # Bleibrey, Mark - 2219 - .31
restart_port("Gi1/0/15") # Weight Room Desk - 1240 - .31
restart_port("Gi1/0/17") # Weight Room - 1240 - .31

connect_to("HS-IDF4-2960X-Stack") # HS Library
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/5") # Olson, Sarah - 1230 - .41
restart_port("Gi1/0/22") # Hart, Bonnie - 1150 - .41
restart_port("Gi1/0/26") # Connolly, Erin - 1112 - .41
restart_port("Gi2/0/16") # Howe, Christina - 1115 - .41
restart_port("Gi2/0/19") # Coker, Megan - 1220 - .41
restart_port("Gi2/0/22") # Detention - 1111 - .41
restart_port("Gi2/0/26") # Back Stage - 1151 - .41
restart_port("Gi2/0/31") # Chapman, Katie - 1117 - .41
restart_port("Gi2/0/34") # Long, Jill - 1116 - .41
restart_port("Gi2/0/37") # McCullen, Pamela - 1118 - .41
restart_port("Gi3/0/5") # Davis, Dane - 1222 - .41
restart_port("Gi3/0/13") # Hull, Matt - JrSr - 1234 - .41
restart_port("Gi3/0/31") # Auditorium - 1152 - .41
restart_port("Gi3/0/37") # Cafeteria - 1153 - .41
restart_port("Gi3/0/39") # DeStefanis, Jeff (K) - 1214 - .41
restart_port("Gi3/0/41") # Auditorium lobby - 1020 - .41

connect_to("LGHS-IDF5-2960S48-01") # Room 210 - Art Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/24") # Everts, Kimberly - 2213 - .51
restart_port("Gi1/0/32") # Dell'olio, Jennifer - 1107 - .51

connect_to("LGHS-IDF5-2960S48-02") # Room 210 - Art Room
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/21") # Canale, Katie - 1110 - .52
restart_port("Gi1/0/24") # Greene, Vicky - 2212 - .52

connect_to("LGHS-IDF6-2960S24-02") # Room 200 - Business Lab
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/12") # Wilson, Kemm - 1216 - .63
restart_port("Gi1/0/15") # Bennett, Jeffrey - 1103 - .63
restart_port("Gi1/0/17") # Martineau, Nathalie - 2202 - .63
restart_port("Gi1/0/19") # Armstrong, Jedidiah - 1101 - .63
restart_port("Gi1/0/20") # Fournier, Michelle - 1102 - .63
restart_port("Gi1/0/21") # Breslin, Karen - 2201 - .63
restart_port("Gi1/0/23") # Hoffman, Brenda - 2200 - .63

connect_to("LGHS-IDF7-2960S48-01") # Room 1 - SP ED
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/3") # Dempsey, Cheri - 1004 - .71
restart_port("Gi1/0/5") # Burrall, Kevin - 1005 - .71
restart_port("Gi1/0/6") # Brown, William - 1003 - .71
restart_port("Gi1/0/16") # Darby, Tammy - 1007 - .71
restart_port("Gi1/0/17") # Wells, Roger - 1010 - .71
restart_port("Gi1/0/19") # Round, Nicholas - 1001 - .71
restart_port("Gi1/0/20") # Room 006 - 1232 - 1002 - .71
restart_port("Gi1/0/37") # Clothier, Rick - 1219 - .71
restart_port("Gi1/0/40") # Mondella, Christopher - 1002 - .71
restart_port("Gi1/0/44") # McGrath, Nicole - 1009 - .71
restart_port("Gi1/0/46") # Spath, Robert - 1008 - .71
