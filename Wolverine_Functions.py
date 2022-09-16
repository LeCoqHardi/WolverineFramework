#functions file
from simple_term_menu import TerminalMenu
import os
import Scripts.BruteforceChoice as bfc
import Scripts.BruteforceHydra as bfh
import Scripts.BruteforceMedusa as bfm
import Scripts.BruteforcePatator as bfp
import Scripts.DDOS_ICMP as ddos
import Scripts.Ettercap as ett
import Scripts.MacChanger as mcc
import Scripts.MSFVenomAndroid as msfva
import Scripts.MSFVenomWindows as msfw
import Scripts.NetworkScan as nws
import Scripts.WPScan as wpsc

def ReturnToMenu():
    print("Do you want to go back to main menu or quit Wolverine ?\n")
    options = ["Main Menu", "Quit Wolverine"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    UserChoice = options[menu_entry_index]
    if (UserChoice == "Main Menu"):
        os.system("wolverine")
    else:
        exit()

def AttackPerformed(Choice):
    # MITM choice
    if(Choice == "Man in The Middle Attack"):
        ett.MiTM_Attack()

        ReturnToMenu()
        
    # -------------------------------------
        
    # DDOS choice
    elif(Choice == "DoS / DDoS"):
        ddos.DDOS_ICMP()

        ReturnToMenu()

    # -------------------------------------

    # Bruteforce Choice
    elif(Choice == "Bruteforce"):
        BRUTEFORCEAPP = bfc.BruteforceChoice()
        print(BRUTEFORCEAPP)
        if(BRUTEFORCEAPP == "Medusa"):
            bfm.BruteforceMedusa()

        elif(BRUTEFORCEAPP == "Hydra"):
            bfh.BruteforceHydra()
        elif(BRUTEFORCEAPP == "Patator"):
            bfp.BruteforcePatator()
    
        ReturnToMenu()
    # -------------------------------------
            
    # Network Scanning Choice
    elif(Choice == "Network Scanning"):
        nws.NetworkScan()

        ReturnToMenu()

    # MSFConsole Choice
    elif(Choice == "Launch Metasploit"):
        print("Launching MSFConsole...")
        os.system("sudo service postgresql start")
        os.system("sudo msfconsole -q")
        ReturnToMenu()
    # -------------------------------------

    # Doxing Choice
    elif(Choice == "Doxing from a phone number"):
        print("Please type the phone number you want to Dox (with country code [+..])")
        PhoneNumber = input("WolverineFramework - \033[1;4m Phone Number \033[0m > ")
        command = "./Scripts/phoneinfoga scan -n " + PhoneNumber
        os.system(command)
        ReturnToMenu()
    # -------------------------------------
    
    # WPScan Choice
    elif(Choice == "Scan wordpress vulnerabilities"):
        print("choice = wordpress")

        ReturnToMenu()

    #Mac Changer Choice
    elif(Choice == "Hide your MAC Adress with a fake MAC Adress"):
        print("choice = Hide your MAC Adress with a fake MAC Adress")

        ReturnToMenu()

    # Remote Control Choice
    elif(Choice == "Take remote control of a device"):
        print("choice = Take remote control of a device")

        ReturnToMenu()

    # Quit Wolverine Choice
    elif(Choice == "Quit Wolverine"):
        print("choice = Quit Wolverine")
        exit()
        
    else:
        print("error.")
        exit()