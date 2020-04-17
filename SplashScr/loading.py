import os
import time

def loading_bar(seconds):
  for loading in range(0,seconds+1):
    percent = (loading * 100) // seconds
    print("\n")
    print("Loading...")
    print("<" + ("-" * loading) + (" " * (seconds-loading)) + "> " + str(percent) + "%")
    print("\n")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  
  
  
  
#Main Code Start
loading_bar(10)

print ("\nYour code begins here...")
