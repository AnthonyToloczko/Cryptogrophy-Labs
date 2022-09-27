import random

# Creates the key used for encrypting the program
def generateKey(keyLength):
    key = list("")
    counter = 0
    while counter < keyLength:
        diceRoll = random.randint(97, 123)
        character = chr(diceRoll)
        key.append(character)
        counter = counter + 1
    print(key)
    return ("".join(key))

# Encrypts the plain text
def cipherText(string, key):
    cipher_text = []
    counter = 0
    keyCounter = 0
    while counter < len(string):
        if ord(string[counter]) in range(97, 123):
            x = (ord(string[counter]) - 96) + (ord(key[keyCounter]) - 96)
            if x <= 26:
                x = x + 96
            else:
                x = x - 26
                x = x + 96
            cipher_text.append(chr(x))
            counter = counter + 1
            if keyCounter < (len(key) - 1):
                keyCounter = keyCounter + 1
            else:
                keyCounter = 0
        elif ord(string[counter]) in range(65, 91):
            x = (ord(string[counter]) - 64) + (ord(key[keyCounter]) - 96)
            if x <= 26:
                x = x + 64
            else:
                x = x - 26
                x = x + 64
            cipher_text.append(chr(x))
            counter = counter + 1
            if keyCounter < (len(key) - 1):
                keyCounter = keyCounter + 1
            else:
                keyCounter = 0
        elif string[counter] == "\n" or string[counter] == "\t":
            #cipher_text.append(string[counter])
            counter = counter + 1
        else:
            cipher_text.append(string[counter])
            counter = counter + 1
    return ("".join(cipher_text))


# Decrypts the ciphertext
def originalText(cipher_text, key):
    orig_text = []
    counter = 0
    keyCounter = 0
    while counter < len(cipher_text):
        if ord(cipher_text[counter]) in range(97, 123):
            x = (ord(cipher_text[counter]) - 96) - (ord(key[keyCounter]) - 96)
            if x > 0:
                x = x + 96
            else:
                x = x + 26
                x = x + 96
            orig_text.append(chr(x))
            counter = counter + 1
            if keyCounter < (len(key) - 1):
                keyCounter = keyCounter + 1
            else:
                keyCounter = 0
        elif ord(cipher_text[counter]) in range(65, 91):
            x = (ord(cipher_text[counter]) - 64) - (ord(key[keyCounter]) - 96)
            if x > 0:
                x = x + 64
            else:
                x = x + 26
                x = x + 64
            orig_text.append(chr(x))
            counter = counter + 1
            if keyCounter < (len(key) - 1):
                keyCounter = keyCounter + 1
            else:
                keyCounter = 0
        elif cipher_text[counter] == "\n" or cipher_text[counter] == "\t":
            counter = counter + 1
        else:
            orig_text.append(cipher_text[counter])
            counter = counter + 1
    return ("".join(orig_text))


# Driver code
def main():
    print("Input an HTML filename: ")
    #filename = input()
    #file = open(filename)
    file = open("practice.html")
    print("Input how long you wabt the key to be")
    #keyLength = input()
    keyLength = 8
    string = ""
    while file.readline() != "":
        fileCharacter = file.readline()
        string = string + fileCharacter
    file.close
    key = generateKey(keyLength)
    cipher_text = cipherText(string,key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))
main()