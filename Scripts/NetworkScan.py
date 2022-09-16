#!/usr/bin/env python3
from turtle import clear
from simple_term_menu import TerminalMenu
import os
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def NetworkScan():

    print("What do you want to scan ?")
    print("\x1B[3mnote from the dev, network scans generates a lot of network traffic and aren't discrete, be careful of what you're doing with it.")
    options = ["One single host", "All hosts in a LAN"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    UserChoice = options[menu_entry_index]

    if(UserChoice == "One single host"):
        print("What is the domain name/IP/Hostname of your target ?")
        IP = input("WolverineFramework - \033[1;4m IP \033[0m > ")
        print("--------------------------------------------------")
        print("What type of scan do you want to perform ?")
        print("\x1B[3mnote from the dev 2, classic scans takes less time than aggressive scans, even if they are less accurate. ")
        options = ["Classic (Shows Open Ports)", "Aggresive (Show Open Ports + Services behind them)"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        UserChoice2 = options[menu_entry_index]
        if(UserChoice2 == "Classic (Shows Open Ports)"):
            print("Launching classic scan using nmap...")
            command = "nmap " + IP
            os.system(command)

        elif(UserChoice2 == "Aggresive (Show Open Ports + Services behind them)"):
            print("Lauching aggressive scan using nmap...")
            command = "nmap -A " + IP
            os.system(command)

    elif(UserChoice == "All hosts in a LAN"):
        IP = get_ip()
        print("--------------------------------------------------")
        print("What app do you want to use for your scan ?")
        options = ["NMAP (IP Address + Host brand)", "Arp-Scan (MAC Address + IP Address + Host brand)"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        UserChoice2 = options[menu_entry_index]
        if(UserChoice2 == "NMAP (IP Address + Host brand)"):
            print("Launching scan using nmap...")
            command = "nmap " + IP + "/24"
            os.system(command)

        elif(UserChoice2 == "Arp-Scan (MAC Address + IP Address + Host brand)"):
            print("Lauching scan using Arp-Scan...")
            command = "sudo arp-scan -l"
            os.system(command)
