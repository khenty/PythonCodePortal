encrypt = input("Enter a sentence to encrypt:\n ")


encrypted_text = ""
for c in encrypt:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

print("\n")

decrypt = input("Enter encrypted text to decrypt:\n ")

plain_text = ""
for c in decrypt:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)
