# INFO #
# [+] Created by Fattcat -----> https://github.com/Fattcat

# NEED TO INSTALL #
# - pyfiglet
# - colorama
# - platform
# - subprocess

# Modules
# +------------------------------------+
import os              	             #-+
from time import sleep 	             #-+
import platform        	             #-+
import subprocess                    #-+
from colorama import Fore, init      #-+
from pyfiglet import figlet_format   #-+
# +------------------------------------+


# Colors
# +------------------------------------+
black = '\033[30m'	                 #-+
red = '\033[31m'	                 #-+
green = '\033[32m'	                 #-+
yellow = '\033[33m'	                 #-+
orange = '\033[33m\033[31m'          #-+
blue = '\033[34m'	                 #-+
magenta = '\033[35m'	             #-+
cyan = '\033[36m'	                 #-+
white = '\033[37m'	                 #-+
reset = '\033[0m'                    #-+
# +------------------------------------+

# StegHide Commands
Hide_Steg_Password = ''
Extr_Steg_Password = ''

# Clear by OS
# +------------------------------------+
def Linux_CLEAR():                   #-+
    sleep(1)                         #-+
    os.system('clear')               #-+
    sleep(0.2)                       #-+
                                     #-+
def Windows_CLEAR():                 #-+
    sleep(1)                         #-+
    os.system('cls')                 #-+
    sleep(0.2)                       #-+
# +------------------------------------+

#Defined Text For show in Terminal Linux ONLY ! - Sorry Windows :/

# Detecting OS
def CheckOS():
    OperationSystem = platform.system()
    release = platform.release()

    if OperationSystem == 'Windows':
        if '10' in release:
            detected_os = 'Windows 10'
            Windows_CLEAR()
        else:
            detected_os = 'Windows (Version Lower than Windows 10)'
            Windows_CLEAR()
    elif OperationSystem == 'Linux':
        Linux_CLEAR()
        if 'kali' in release.lower():
            detected_os = 'Kali Linux'
            Linux_CLEAR()
        elif 'arch' in release.lower():
            detected_os = 'Arch Linux'
            Linux_CLEAR()
        else:
            detected_os = 'Linux'
            Linux_CLEAR()
    else:
        detected_os = 'UNKNOWN OS'

# ---------------------------------------------------------------- # 
#                          Toto asi NEtreba
#    for ClearIt in "Linux", "arch", "Kali Linux", "Arch Linux":
#        os.system("clear")
#        Linux_CLEAR()
# ---------------------------------------------------------------- #
    print('+ --------------------------- +', ' '*10)
    print(f'+ - {orange}Detected OS{reset} :' ,f'{green}{OperationSystem}{reset} - +')
    if OperationSystem =="Linux":
        print('\n(it is better in some cases than Windows 10)')
        sleep(1)
        Kali_Linux()
        sleep(1)
    elif OperationSystem ==" Windows":
        print('Bruhh ... Windows But OK Lets GO.')
        sleep(1)
        Windows_CLEAR()
        sleep(1)
    sleep(1)

# Inicializácia knižnice Colorama
init(autoreset=True)
text_to_colorize = "[ + ] PyHider [ + ]"
# Vytvorenie veľkého textu pomocou pyfiglet
big_text = figlet_format(text_to_colorize)
# Farebný text
colored_text = f"{Fore.GREEN}{big_text}{Fore.RESET}"
print(colored_text)

def UseMenu():
    print(f'          [+] {green}Command --> Use {reset}[+]')
    print(f'+ --------------------------------------------------------- +')
    print(f'+ Extr_Steg_Password --> GET Hidden Password FROM Image     +')
    print(f'+ Hide_Steg_Password --> HIDE Password TO Your Image        +')
    print(f'+ -h or --help --> Show Again this for Help                 +')
    print(f'+ -e or exit for exit this script :D                        +')
    print(f'+ --------------------------------------------------------- +')

# StegHide Commands
Hide_Steg_Password = f'steghide embed -ef', {FileName}, '-cf', {ImageName}
Extr_Steg_Password = f'steghide extract -sf', {ImageName}


def MainMenu():
    print(f'{magenta}[{reset}{yellow}+{reset}{magenta}]{reset}', ' ', '-'*60, ' ', f'{magenta}[{reset}{yellow}+{reset}{magenta}]{reset}')
    print(f'                        [-+-] Welcome to PyHider [-+-]')
    print(f'{magenta}[{reset}{yellow}+{reset}{magenta}]{reset}' ,' ' *20 , f'Created by Fattcat' , ' '*20 , f'{magenta}[{reset}{yellow}+{reset}{magenta}]{reset}')
    print(f'[+', ' ','-'*60,' ','+]')
    print(f'Select Option or type {green}-h{reset} or {green}--help{reset} for show available commands')
    FirstUserInput = input('--> ')
    if FirstUserInput =='-h' or FirstUserInput =='--help' or FirstUserInput =='help':
        UseMenu()
    elif FirstUserInput == 'Extr_Steg_Password':
        os.popen(StegCommand).read() 


def Windows_10():
    Windows_CLEAR()
    MainMenu()


def Kali_Linux():
    Linux_CLEAR()
    MainMenu()


while True:
    CheckOS()
    sleep(2)
    MainMenu()
