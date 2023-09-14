# INFO #
# [+] Created by Fattcat -----> https://github.com/Fattcat

# NEED TO INSTALL #
# - pyfiglet
# - os
# - colorama
# - platform
# - subprocess

import os
import platform
from time import sleep
from colorama import Fore, init
from pyfiglet import figlet_format

# Inicializace knihovny Colorama
init(autoreset=True)
text_to_colorize = "[ + ] PyHider [ + ]"
# Vytvoření velkého textu pomocí pyfiglet
big_text = figlet_format(text_to_colorize)
# Farebný text
colored_text = f"{Fore.GREEN}{big_text}{Fore.RESET}"
print(colored_text)

# Funkce pro čištění konzole v různých operačních systémech
def clear_console():
    sleep(1)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    sleep(0.2)

# Funkce pro kontrolu operačního systému
def check_os():
    detected_os = platform.system()
    release = platform.release()

    if detected_os == 'Windows':
        if '10' in release:
            detected_os = 'Windows 10'
        else:
            detected_os = 'Windows (verze nižší než Windows 10)'
    elif detected_os == 'Linux':
        if 'kali' in release.lower():
            detected_os = 'Kali Linux'
        elif 'arch' in release.lower():
            detected_os = 'Arch Linux'
        else:
            detected_os = 'Linux'
    else:
        detected_os = 'NEZNÁMÝ OS'

    clear_console()
    print(' ' * 17, '+ ------------------------------------ +')
    print(f'                         + - {Fore.YELLOW}Detected OS{Fore.RESET}:', f'{Fore.GREEN}{detected_os}{Fore.RESET} - +')
    print(' ' * 17, '+ ------------------------------------ +')

    print('+ ------------------------------------------------------------------------ +')
    print('   Skvělé! Máte operační systém Linux (v některých případech lepší než Windows 10).')
    print('+ ------------------------------------------------------------------------ +')

check_os()
sleep(2)

# Funkce pro hlavní menu (s přidanou smyčkou)
def main_menu():
    while True:
        print(f' ' * 20, '[+] [-+-] Vítejte v aplikaci PyHider [-+-] [+]')
        print(f' ' * 25, '[+]', f'{Fore.RED}Vytvořil{Fore.RESET}', f'{Fore.BLUE}NĚKDO{Fore.RESET}', '[+]\n')
        print(f'Vyberte možnost nebo zadejte {Fore.GREEN}-h{Fore.RESET} nebo {Fore.GREEN}--help{Fore.RESET} pro zobrazení dostupných příkazů')
        first_user_input = input(f'{Fore.YELLOW}--> ')
        
        if first_user_input == '-h' or first_user_input == '--help':
            use_menu()
        elif first_user_input == 'Hide_Steg_Password':
            hide_steg_password()
        elif first_user_input == 'Extr_Steg_Password':
            extr_steg_password()
        elif first_user_input == '-e' or first_user_input == 'exit':
            exit()
        else:
            print('Neplatný vstup, zadejte platný příkaz.')

# Funkce pro menu "Use"
def use_menu():
    print(f'[+] {Fore.GREEN}Příkaz --> Use {Fore.RESET}[+]')
    print(f'+ --------------------------------------------------------- +')
    print(f'+ Hide_Steg_Password --> Skryj heslo do obrázku                +')
    print(f'+ Extr_Steg_Password --> Získat skryté heslo z obrázku         +')
    print(f'+    -h nebo --help  --> Zobrazit znovu toto nápovědní menu   +')
    print(f'+     -e nebo exit   --> Ukončit skript :D                    +')
    print(f'+ --------------------------------------------------------- +')

# Funkce pro skrytí hesla do obrázku
def hide_steg_password():
    print('Zadejte název textového souboru')
    txt_file_name = input('--> ')
    print('Zadejte nové heslo (uložte si ho pro budoucnost)')
    password = input('--> ')
    print('Zadejte název obrázku')
    image_name = input('--> ')
    command_for_hide = f"steghide embed -ef {txt_file_name} -cf {image_name} -p {password}"

    os.popen(command_for_hide).read()
    input('Stiskněte Enter pro návrat do hlavního menu.')

# Funkce pro získání skrytého hesla z obrázku
def extr_steg_password():
    print('Zadejte název textového souboru')
    txt_file_name = input('--> ')
    print('Zadejte heslo')
    password = input('--> ')
    print('Zadejte název obrázku (s příponou obrázku)')
    image_name = input('--> ')
    command_for_extract = f'steghide extract -sf {image_name} -p {password}'
    os.popen(command_for_extract).read()
    input('Stiskněte Enter pro návrat do hlavního menu.')

# Spuštění hlavního menu

main_menu()
