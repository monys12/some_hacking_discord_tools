import requests
import os
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


                                                                                                              
                                                   \033[31m ♥ v 2.00 ♥\033[39m 

                                            \033[33m>>\033[39m  \033[36mMade by Anonymous\033[39m \033[33m<<\033[39m            
""")

web = input("\033[32m>\033[39m Enter the Webhook To Delete it :  ")



def delet():
    requests.delete(web)
    cheak = requests.get(web)
    if cheak.status_code == 404:
        print("[+] \033[32mWEBHOOK SUCCESFULLY DELETED\033[39m ")
        os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
    elif cheak.status_code == 200:
        print("[-]\033[31m FAILED TO DELETE WEBHOOK ")    
        os.system("pause >nul")
test = requests.get(web)
if test.status_code == 404:
    print("\033[31m[-]\033[39m THE WEBHOOK IS INVALID : ")
    os.system("pause >nul")
elif test.status_code == 200:
    print("\033[35m>\033[39m THE WEBHOOK IS VALID : ")
    delet()
        


