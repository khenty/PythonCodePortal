#Stores the morse code for the alphabet using a dictionary
morseCode = {"A":".-","B":"-...","C":"-.-."}
morseCode["D"] = "-.."
morseCode["E"] = "."
morseCode["F"] = "..-."
morseCode["G"] = "--."
morseCode["H"] = "...."
morseCode["I"] = ".."
morseCode["J"] = ".---"
morseCode["K"] = "-.-"
morseCode["L"] = ".-.."
morseCode["M"] = "--"
morseCode["N"] = "-."
morseCode["O"] = "---"
morseCode["P"] = ".--."
morseCode["Q"] = "--.-"
morseCode["R"] = ".-."
morseCode["S"] = "..."
morseCode["T"] = "-"
morseCode["U"] = "..-"
morseCode["V"] = "...-"
morseCode["W"] = ".--"
morseCode["X"] = "-..-"
morseCode["Y"] = "-.--"
morseCode["Z"] = "--.."

#Stores numbers 0 to 9
morseCode["1"] = ".----"
morseCode["2"] = "..---"
morseCode["3"] = "...--"
morseCode["4"] = "....-"
morseCode["5"] = "....."
morseCode["6"] = "-...."
morseCode["7"] = "--..."
morseCode["8"] = "---.."
morseCode["9"] = "----."
morseCode["0"] = "-----"

#Allow spaces in the Morse
morseCode[" "] = " "

#Retrieve user's message and convert it to upper case.
message = input("Enter message to convert to Morse: ").upper()
encodedMessage = ""

#Convert each letter into morse code:
for character in message:
  #Check that the character is in the moreCode dictionary (e.g letter of the alphabet)
  if character in morseCode:
    encodedMessage += morseCode[character] + " "
  else:
    #Replace unrecognised characters with a question marks
    encodedMessage += "???"
    
#Display the message in morse code:
print("\nYour message in morse code is:\n")
print(encodedMessage)
