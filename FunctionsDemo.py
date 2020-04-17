def pause():
    input("\n\nPress any key to continue...\n\n")

def quitMessage():
    print ("Thank you for using this program")
    print ("Goodbye")
    
def printThreeLines():
    for i in range(1,4):
        print ('this is line ' + str(i))

def printNineLines():
    for i in range(1,4):
        printThreeLines()

def startMessage():
    print ("This program demonstrates the use of Python functions")
    pause()
    
def blank_Line():
    print()
    
def clearScreen():
    for i in range(1,26):
        blank_Line()



startMessage()
clearScreen()
print ("Functions Demo\n")
printNineLines()
pause()
clearScreen()
printNineLines()
blank_Line()
printNineLines()
pause()
clearScreen()
quitMessage()
