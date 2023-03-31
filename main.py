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
os.system("cls")

print("""

\033[33m

                 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
                ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║╚██╗ ██╔╝████╗ ████║██╔═══██╗██║   ██║██╔════╝
                ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║   ██║███████╗
                ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║   ██║╚════██║
                ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║
                ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝

                 \033[39m                                \033[31m♥ v 2.00 ♥\033[39m                                                   


""")



print("""

1 \033[32m>\033[39m  Webhook deleter 
2 \033[32m>\033[39m  Webhook cheaker 
3 \033[32m>\033[39m  Webhook spammer
\033[36m--------------------\033[39m
4 \033[35m>\033[39m  Token bruteforce
5 \033[35m>\033[39m  Token Login and Info
6 \033[35m>\033[39m  Token cheaker
\033[35m--------------------\033[39m
7 \033[31m>\033[39m DDos Expert


""")
chinpute = input("\033[34m>\033[39m Select Number : ")

if chinpute == "1":
    os.system("start python webhook_deleter.py")

elif chinpute == "2":
    os.system("start python webhook_cheaker.py")

elif chinpute == "3":
    os.system("start python webhook_spmamer.py")

elif chinpute == "4":
    os.system("start python token_brute_forcing.py") 

elif chinpute =="5":
    os.system("start python token_login.py")

elif chinpute == "6":
    os.system("start python token_cheaker.py")

elif chinpute == "7":
    os.system("start python ddos_expert.py")        



