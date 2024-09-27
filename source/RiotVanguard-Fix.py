import re
from os import system
import os
import time
import sys
import platform
import colorama
from colorama import Fore, init, Style
import win32ui
import requests
import subprocess

mytitle = "3n3scan's Riot Vanguard Tool"


## Console Input Echos ##
ENTER_CHOICE_CONSOLE_ECHO = (f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Enter the number of your choice:{Style.RESET_ALL} """)


def deactivate_riotvanguard():
    try:
        subprocess.run(["net", "stop", "vgc"], check=True)
        subprocess.run(["net", "stop", "vgk"], check=True)

        win32ui.MessageBox(f'Done. Stopped Riot Vanguard Services.\nGoing to Main Page in 5 Seconds...', f"{mytitle}")
        time.sleep(5)
        main()

    except subprocess.CalledProcessError as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(3)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()


def delete_riotvanguard():
    try:
        subprocess.run(["sc", "delete", "vgc"], check=True)
        subprocess.run(["sc", "delete", "vgk"], check=True)
        subprocess.run(["takeown", "/f", "C:\\Program Files\\Riot Vanguard", "/r", "/d", "y"], check=True)
        subprocess.run(["icacls", "C:\\Program Files\\Riot Vanguard", "/grant", "administrators:F", "/t"], check=True)
        subprocess.run(["rmdir", "/s", "/q", "C:\\Program Files\\Riot Vanguard"], check=True)

        win32ui.MessageBox(f'Done. Deleted:\n- Riot Vanguard Services\n- Riot Vanguard + Folder\n\nGoing to Main Page in 5 Seconds...', f"{mytitle}")
        time.sleep(5)
        main()

    except subprocess.CalledProcessError as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(3)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()


def controlpanel():
    try:
        subprocess.run(["control", "appwiz.cpl"])

        win32ui.MessageBox(f'Done. Opened Control Panel.\nGoing to Main Page in 5 Seconds...\n', f"{mytitle}")
        time.sleep(5)
        main()

    except subprocess.CalledProcessError as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(3)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()


def informations():
    try:
        print(f"")
        print(f"3n3scan's Riot Vanguard Tool - Informations")
        print(f"-------------------------------------------")
        print(f"- Developed by: 3n3scan")
        print(f"- Version: 1.0")
        print(f"- Date: 2021-07-01")
        print(f"- Description: This script is used to deactivates and delete Riot Vanguard + Services")
        print(f"- Features:")
        print(f"  - Deactivates and Stops the Riot Vanguard Services")
        print(f"  - Deletes the Riot Vanguard Services Riot and Vanguard")
        print(f"  - Open Control Panel")
        print(f"")
        print(f"Going to Main Page in 5 Seconds...")
        
        time.sleep(5)
        main()

    except requests.RequestException as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(3)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()


def exit_script():
    system("cls")
    win32ui.MessageBox(f"Exiting... Thank you for using this script!", f"{mytitle}")
    sys.exit()
    

def main():
    system("title "+mytitle)
    os = platform.system()
    current_date = time.strftime("%d.%m.%Y")
    current_time = time.strftime("%H:%M:%S")
    if os == "Windows":
        system("cls")
    else:
        system("clear")
        print(chr(27) + "[2J")
    print(f"""{Fore.CYAN}
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

        ██████╗ ██╗ ██████╗ ████████╗██╗   ██╗ █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
        ██╔══██╗██║██╔═══██╗╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
        ██████╔╝██║██║   ██║   ██║   ██║   ██║███████║██╔██╗ ██║██║  ███╗██║   ██║███████║██████╔╝██║  ██║
        ██╔══██╗██║██║   ██║   ██║   ╚██╗ ██╔╝██╔══██║██║╚██╗██║██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
        ██║  ██║██║╚██████╔╝   ██║    ╚████╔╝ ██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
        ╚═╝  ╚═╝╚═╝ ╚═════╝    ╚═╝     ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 

                                            ███████╗██╗██╗  ██╗
                                            ██╔════╝██║╚██╗██╔╝
                                            █████╗  ██║ ╚███╔╝
                                            ██╔══╝  ██║ ██╔██╗
                                            ██║     ██║██╔╝ ██╗
                                            ╚═╝     ╚═╝╚═╝  ╚═╝
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Style.RESET_ALL}
                                    {Fore.LIGHTGREEN_EX} > 3n3scan's Riot Vanguard Tool <{Style.RESET_ALL}
                                        {Fore.MAGENTA} > Developed by: 3n3scan <{Style.RESET_ALL}
                                        {Fore.MAGENTA} > {current_date} | {current_time} <{Style.RESET_ALL}
                                        
{Fore.CYAN}> Choose an option:{Style.RESET_ALL}
{Fore.GREEN}> [1] Deactivate Riot Vanguard{Style.RESET_ALL}
{Fore.LIGHTBLUE_EX}> [2] Delete Riot Vanguard{Style.RESET_ALL}
{Fore.LIGHTMAGENTA_EX}> [3] Open Control Panel{Style.RESET_ALL}
{Fore.YELLOW}> [4] Informations{Style.RESET_ALL}
{Fore.RED}> [5] Exit Script{Style.RESET_ALL}
""")

    choice = input(ENTER_CHOICE_CONSOLE_ECHO)

    if choice == "1":
        deactivate_riotvanguard()
    elif choice == "2":
        delete_riotvanguard()
    elif choice == "3":
        controlpanel()
    elif choice == "4":
        informations()
    elif choice == "5":
        exit_script()
    else:
        print(f"{Fore.RED}> Invalid choice. Please enter '{Fore.CYAN}1{Fore.RED}', '{Fore.CYAN}2{Fore.RED}', '{Fore.CYAN}3{Fore.RED}', '{Fore.CYAN}4{Fore.RED}' or '{Fore.CYAN}5{Fore.RED}' <{Style.RESET_ALL}")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()
