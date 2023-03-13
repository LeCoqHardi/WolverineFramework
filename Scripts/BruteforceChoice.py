#!/usr/bin/env python3
from simple_term_menu import TerminalMenu

def BruteforceChoice():
    print("Which bruteforce app do you want to use ?")
    print("---------------------------------\n")
    options = ["Medusa", "Hydra", "Patator"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    UserChoice = options[menu_entry_index]
    return UserChoice