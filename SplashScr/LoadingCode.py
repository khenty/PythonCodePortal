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
  
  
def loading_screen(seconds):
    screens=open("dragon2.txt", 'r')
    for lines in screens:
        print(lines, end='')
        time.sleep(seconds)
    screens.close()

  
#Main Code Start
loading_bar(10)
os.system('cls' if os.name == 'nt' else 'clear')
loading_screen(.5)


print ("\n\nEeek! A firey dragon! What now...?")
