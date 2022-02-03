# Crypto Terminal: Console
# Author: Thomas Hart
# Created: February 2nd, 2022
# Modified: February 2nd, 2022

import os

class Console():

    def __init__(self):
        self.dir = "~"

    def start(self):
        print(f"crypto-terminal:{self.dir}$ ", end = '')
        self.get_input()
    
    def get_input(self):
        ipt = input().strip().lower().split()
        if len(ipt) == 0:
            self.start()
        # elif ipt[0] == "cd":
        #     if len(ipt) == 1:
        #         self.change_dir("")
        #     else:
        #         self.change_dir(ipt[1])
        elif ipt[0] == "exit":
            exit()
        elif ipt[0] == "help":
            self.help()
        else:
            self.error(ipt[0])
    
    # def change_dir(self, new_dir):

    #     if new_dir == "~" or new_dir == "" or new_dir == "~/":
    #         self.dir = "~"
    #     else:
    #         self.dir += new_dir
    #     self.start()

    def help(self):
        with open ("help.txt") as f:
            for line in f:
                print(line, end = '')
            print()
        self.start()

    def error(self, err):
        print(f"\"{err}\" is not a recognized command.")
        print("For a list of available commands, use \"help\".")
        self.start()