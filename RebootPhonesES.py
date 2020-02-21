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

restart_port("Gi1/0/8") # Schenk, Kenneth - 4531 - .4
restart_port("Gi1/0/16") # Mason, Susan - 4532 - .4
restart_port("Gi1/0/28") # Alex Poetzsch - 4301 - .4
restart_port("Gi1/0/30") # Helms, Faith Back Office - 4017 - .4
restart_port("Gi1/0/40") # Gearing, Cassamira - 4302 - .4
restart_port("Gi1/0/41") # Abrantes/Jaeger - 4308 - 4307 - .4
restart_port("Gi1/0/42") # McIntosh, Morgan - 4307 - .4
restart_port("Gi1/0/45") # Coker, Megan - 1220 - .4
restart_port("Gi1/0/46") # Way, Janine - 4511 - .4
restart_port("Gi1/0/47") # Hull, Matt - ES - 1234 - .4

connect_to("LGES-MDF-2960S48-01") # ES MDF
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # Little Theater - 4533 - .2
restart_port("Gi1/0/2") # Conway, James - 4010 - .2
restart_port("Gi1/0/3") # Fox, Lisa - 4000 - .2
restart_port("Gi1/0/7") # Mondschein, Ginny - 4004 - .2
restart_port("Gi1/0/9") # Gunther, Sandy - 4051 - .2
restart_port("Gi1/0/10") # Helms, Faith Back Office 2 - 4017 - .2
restart_port("Gi1/0/11") # File Room - 4009 - .2
restart_port("Gi1/0/17") # Powers, Yvonne - 4542 - .2
restart_port("Gi1/0/18") # Polimeni, Kimberly - 4001 - .2
restart_port("Gi1/0/19") # Fullen, Natalie - 1211 - .2
restart_port("Gi1/0/20") # Helms, Faith Desk - 4017 - .2
restart_port("Gi1/0/24") # YMCA, Afterschool Rm - 4310 - .2
restart_port("Gi1/0/25") # 4309 - .2
restart_port("Gi1/0/33") # Student Phone - 4007 - .2
restart_port("Gi1/0/36") # Zehr, Anna - 4305 - .2
restart_port("Gi1/0/37") # Darbee-Laurin, Alison - 4541 - .2
restart_port("Gi1/0/39") # Kelly, Krista - 4306 - .2
restart_port("Gi1/0/40") # Price, Katy - 4548 - .2
restart_port("Gi1/0/41") # Cafeteria Conference - 4053 - .2
restart_port("Gi1/0/42") # Borie, Nicole - 4304 - .2
restart_port("Gi1/0/43") # Moellman, Ann - 4006 - .2
restart_port("Gi1/0/45") # Dudla, Kellie - 4303 - .2
restart_port("Gi1/0/46") # Cafeteria - 4052 - .2
restart_port("Gi1/0/48") # Zivica, Gail - 4609 - .2

connect_to("LGES-IDF1-2960S48-01") # ES IDF1 Reading Center
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/4") # Intermediate 1 Breakout Rm - 4545 - .12
restart_port("Gi1/0/19") # Spring, Kerri - 4107 - .12
restart_port("Gi1/0/20") # Bizan, Geoff - 4210 - .12
restart_port("Gi1/0/23") # ES Staff Lounge - 4020 - .12
restart_port("Gi1/0/24") # Gershen, Ashley - 4201 - .12
restart_port("Gi1/0/29") # Aspland, Kathy - 4202 - .12
restart_port("Gi1/0/30") # Allen, Jeffrey - 4203 - .12
restart_port("Gi1/0/31") # Drapeau, Alyssa - 4207 - .12
restart_port("Gi1/0/32") # Lindsay, Lisa - 4205 - .12
restart_port("Gi1/0/33") # Quillinan/Kelly/Galkiewicz - 4206 - .12
restart_port("Gi1/0/34") # 4209 - .12
restart_port("Gi1/0/35") # 4102 - .12
restart_port("Gi1/0/36") # Thomsen, Brian - 4208 - .12
restart_port("Gi1/0/37") # Holderman, Emily - 4204 - .12
restart_port("Gi1/0/38") # Hoover, Erik - 4101 - .12
restart_port("Gi1/0/39") # Intermediate 2 Breakout Rm - 4110 - .12
restart_port("Gi1/0/40") # Whiting, Lynsey - 4543 - .12
restart_port("Gi1/0/41") # Cross/Larson - 4546 - .12
restart_port("Gi1/0/46") # Dell'olio, Jennifer - 1107 - .12
restart_port("Gi1/0/47") # Crotty, Jeff - 4104 - .12
restart_port("Gi1/0/48") # Buckley, Kelly - 4103- .12

connect_to("LGES-IDF1-2960S48-02") # ES IDF1 Reading Center
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # Catarelli, Kelly - 4108 - .12
restart_port("Gi1/0/3") # Lewis, Jonathan - 4105 - .12
restart_port("Gi1/0/4") # Butler, Mathew - 4106 - .12
restart_port("Gi1/0/34") # 4109 - .12

connect_to("LGES-IDF2-2960S48-01") # ES IDF2 Library
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/1") # Gym Boys - 4523 - .23
restart_port("Gi1/0/9") # Bennett, Kim - 4401 - .23
restart_port("Gi1/0/11") # White, Blake - 4521 - .23
restart_port("Gi1/0/13") # Denton, Karl - 4050 - .23
restart_port("Gi1/0/15") # 4409 - .23
restart_port("Gi1/0/18") # Basement - 4608 - .23
restart_port("Gi1/0/19") # 4405 - .23
restart_port("Gi1/0/21") # 4404 - .23
restart_port("Gi1/0/22") # Hendry, Susan - 4402 - .23
restart_port("Gi1/0/39") # Bennett, Kim - 4404 - .23
restart_port("Gi1/0/40") # Usher, Heather - 4522 - .23
restart_port("Gi1/0/41") # Crossman, Bridget - 4513 - .23
restart_port("Gi1/0/43") # Gym Girls - 4524 - .23
restart_port("Gi1/0/47") # Chance, Renee - 4512 - .23
restart_port("Gi1/0/48") # Patrol Office - 4603 - .23

connect_to("LGES-IDF2-2960X-03") # ES IDF2 Library
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

restart_port("Gi1/0/48") # Library Breakout Room - 4514 - .23
