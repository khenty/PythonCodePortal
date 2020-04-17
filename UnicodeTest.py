str1 = "Hello\u2588out there" # solid block within text
print (str1)
str1 = '\u2588\u2588' #two full block characters
print (str1)
print()
print()
print ("two lines of two full blocks")
print (str1)
print (str1)
print()
print()
# Note: a space is \u0020
print ('two lines of two full blocks, two spaces, two full blocks:')
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print (str1)
print (str1)
print()
print()
print ('two lines of two full blocks, the number 17 and two full blocks:')
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020' + '17' + '\u2588\u2588\u2588\u2588'
print (str1)
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print (str1)
