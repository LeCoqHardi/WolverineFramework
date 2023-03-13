#!/bin/env python3

from simple_term_menu import TerminalMenu
import os

print("What do you want to do ?")
options = ["Custom MAC Address", "Random MAC Address"]
terminal_menu = TerminalMenu(options)
menu_entry_index = terminal_menu.show()
UserChoice = options[menu_entry_index]
print("What is the name of your Network Interface (ex : eth0 / enp0s3)")
NetworkInterface = input("WolverineFramework - Network Interface > ")
if(UserChoice == "Custom MAC Address"):
    print("Type your custom MAC Address (??:??:??:??:??:??)")
    MacAddr = input("WolverineFramework - MAC Address > ")
    command_line = "sudo ifconfig " + NetworkInterface + " down"
    #print(command_line)
    os.system(command_line)
    command_line = "sudo macchanger -m " + MacAddr + " " + NetworkInterface
    #print(command_line)
    os.system(command_line)
    command_line = "sudo ifconfig " + NetworkInterface + " up"
    #print(command_line)
    os.system(command_line)
    command_line = "sudo macchanger -s " + NetworkInterface
    #print(command_line)
    os.system(command_line)
elif(UserChoice == "Random MAC Address"):

    command_line = "sudo ifconfig " + NetworkInterface + " down"
    #print(command_line)
    os.system(command_line)
    command_line = "sudo macchanger -r " + NetworkInterface
    os.system(command_line)
    command_line = "sudo ifconfig " + NetworkInterface + " up" 
    os.system(command_line)
    command_line = "sudo macchanger -s " + NetworkInterface
    os.system(command_line)
