import requests
import sys
import os
import time
import json
import threading
from time import sleep

#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'




os.system('cls & mode 75,15 & title Webhook Spammer')


print("""


                                                                                                              
                                                   \033[31m ♥ v 2.01 ♥\033[39m 

                                            \033[33m>>\033[39m  \033[36mMade by Anonymous\033[39m \033[33m<<\033[39m            
""")


mes = input("\033[32m>\033[39m Enter the Spam Message : ")
webhook = input("\033[32m>\033[39m Enter The Discord Webhook : ")

def spam(mes, webhook):
    while True:
        try:
            r = requests.post(webhook, json={"content": mes})
            s = [200, 201 ,204]
            if r.status_code in s:
                print(f"\033[31m Send Message > {mes}")
                b = r.json
            elif r.status_code == 429:
                print(f"ratelimt, retring in {b['retry_after']} seconds ")


        except:
            print("\033[31m Bad webhook > " + webhook)
            time.sleep(5)
            exit()
def spaming():
    for i in range(2):
        threading.Thread(target=spam, args=(mes, webhook,)).start()
spmaamed = 100

while spmaamed == 100:
    spaming()

