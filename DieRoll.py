import os
import time
from random import randint

die     = ["   \n O \n   "]   #1
die.append("  O\n   \nO  ")   #2
die.append("O  \n O \n  O")   #3
die.append("O O\n   \nO O")   #4
die.append("O O\n O \nO O")   #5
die.append("O O\nO O\nO O")   #6

def dice():
  for roll in range(0,15):
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("\n")
    number = randint(0,5)
    print(die[number])
    time.sleep(0.2)
  
#Main Code Begins
dice()
