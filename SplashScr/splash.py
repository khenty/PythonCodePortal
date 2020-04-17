import os
import time

def splash_screen(seconds):
    splash=open("test.txt", 'r')
    for lines in splash:
        print(lines)
        time.sleep(seconds)
    splash.close()
   
  
  
#Main Code Start
os.system('cls' if os.name == 'nt' else 'clear')
splash_screen(.5)

username=input("Type your username:")
