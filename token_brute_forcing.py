import base64, string, random
from clear_screen import clear
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
print("""


                                                                                                              
                                                   \033[31m ♥ v 2.87 ♥\033[39m 

                                            \033[33m>>\033[39m  \033[36mMade by Anonymous\033[39m \033[33m<<\033[39m            
""")


def token_bruteforcer():
    try:
        os.system('cls & mode 75,15 & title token bruteforce')
        

        uuid = str(input('\033[35m>\033[39m Enter The Discord Id : '))
        if uuid == ''.strip():
            input('UUID cannot be empty, press enter to return ')
            token_bruteforcer()

        first_half = base64.b64encode(uuid.encode('utf-8')).decode().rstrip('b"')
        tried = set()
        amount = 0

        while True:
            second_half = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            third_half = ''.join(random.choice('-' + '_' + string.ascii_letters + string.digits) for _ in range(38))
            
            first_second_third = f'{first_half}.{second_half}.{third_half}'

            if first_second_third not in tried:
                tried.add(first_second_third)
                amount +=1
                print(f'{first_second_third} | {amount}')
                with open('tokens.txt', 'a') as tokens:
                    tokens.write(f'{first_second_third}\n')


    except KeyboardInterrupt:
        token_bruteforcer()

token_bruteforcer()