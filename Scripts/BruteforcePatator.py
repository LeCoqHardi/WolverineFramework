#!/usr/bin/env python3
import os

Path = "/home/$USER/WolverineFramework"

def BruteforcePatator():
    print("\033[1;4m BRUTEFORCING USING PATATOR \033[0m")
    print("-------------------------\n")
    print("What is the IP or the hostname of your target ?")
    IP = input("WolverineFramework - \033[1;4m IP \033[0m > ")
    print("What is the session name of your target ?")
    Session = input("WolverineFramework - \033[1;4m Username \033[0m > ")
    print("What is the protocol targetted ?")
    print("\x1B[3mnote from the dev, to see the available protocol, refer to this Github Repository \x1B[0m: https://github.com/lanjelot/patator")
    Protocol = input("WolverineFramework - \033[1;4m Protocol > \033[0m")
    print("Here are your wordlists (path ", Path,"/Wordlists) : ")
    print("\x1B[3m You can obviously use wordlists from a different path, just type the path of the wordlist you want to use \x1B[0m")
    print("--------------------------------------------------------------------\n")
    os.system("ls", Path,"/Wordlists")
    print("")
    print("--------------------------------------------------------------------")
    print("Which Wordlist do you want to use (file path) ?")
    Wordlist = input("WolverineFramework - \033[1;4m FilePath \033[0m > ")

    #os.system("sudo medusa -h", IP, "-u", Session, "-P", Wordlist, "-M", Protocol)
    command = "sudo patator " + Protocol + "_login host=" + IP + " user=" + Session + " password=FILE0 0=" + Wordlist
    os.system(command)

    