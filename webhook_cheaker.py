import requests

import sys
import os
import time
import json
#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'


os.system('cls & mode 75,15 & title Webhook cheaker')

print("""


                                                                                                              
                                                   \033[31m ♥ v 2.87 ♥\033[39m 

                                            \033[33m>>\033[39m  \033[36mMade by Anonymous\033[39m \033[33m<<\033[39m            
""")




web = input("\033[35m>\033[39m Enter The Webhhook To Cheak It : ")

r = requests.get(web)



s = [200, 201 ,204]
g = [401, 429, 505]
if r.status_code in s:
        print(f"[+] \033[32mGood\033[39m")
        b = r.json

elif r.status_code in g:
        print("[-] \033[31mBad\033[39m")    
       