# INFO #
# [+] Created by Fattcat -----> https://github.com/Fattcat

# Modules
# +----------------------------+
import os              	     #-+
from time import sleep 	     #-+
import platform        	     #-+ 
# +----------------------------+


# Colors
# +----------------------------+
black = '\033[30m'	         #-+
red = '\033[31m'	         #-+
green = '\033[32m'	         #-+
yellow = '\033[33m'	         #-+
orange = '\033[33m\033[31m'  #-+
blue = '\033[34m'	         #-+
magenta = '\033[35m'	     #-+
cyan = '\033[36m'	         #-+
white = '\033[37m'	         #-+
reset = '\033[0m'            #-+
# +----------------------------+

# Clear by OS
def Linux_CLEAR():
    os.system('clear')

def Windows_CLEAR():
    os.system('cls')

# Detecting OS
def CheckOS():
    OperationSystem = platform.system()
    release = platform.release()

    if OperationSystem == 'Windows':
        if '10' in release:
            detected_os = 'Windows 10'
        else:
            detected_os = 'Windows (Version Lower than Windows 10)'
    elif OperationSystem == 'Linux':
        if 'kali' in release.lower():
            detected_os = 'Kali Linux'
        elif 'arch' in release.lower():
            detected_os = 'Arch Linux'
        else:
            detected_os = 'Linux'
    else:
        detected_os = 'UNKNOWN OS'

    print('+ --------------------------- +')
    print(f'+ - {orange}Detected OS : {reset}' + {green}OperationSystem{reset} + ' - +')
    print('+ --------------------------- +')
    sleep(1)

def UseMenu():
    print(f'[+] {green}Commands{reset}')
    print('+ ---------------------------------------------- +')
    print('Start_StegHide --> for start')
    print('')
    print('')
    print('+ ---------------------------------------------- +')

def MainMenu():
    print(f'+', ' ', '-'*60, ' ', '+')
    print(f'{magenta}[{reset}{yellow}+{reset}{magenta}]{reset}' ,' ' *20 , 'Created by Fattcat' , ' '*20 , '[+]')
    print('\n')
    print(f'Welcome to PyHider')
    print('\n')
    print(f'[+', ' ','-'*60,' ','+]')
    print('Select option')
    FirstUserInput = input('--> ')
    if FirstUserInput =='-h' or FirstUserInput =='--help' or FirstUserInput =='help':
        UseMenu()

def Windows_10():
    MainMenu()


def Kali_Linux():
    MainMenu()

CheckOS()
sleep(2)
MainMenu()
