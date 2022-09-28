import random
import pathlib

# Creates the key used for encrypting the program
def generateKey(keyLength):
    key = list("")
    counter = 0
    while counter < keyLength:
        diceRoll = random.randint(97, 122)
        character = chr(diceRoll)
        key.append(character)
        counter = counter + 1
    return ("".join(key))
    

# Encrypts the plain text
def cipherText(filePath, keyFile):
    key = ""
    keyCharacter = "place holder"
    while keyCharacter != "":
        keyCharacter = keyFile.readline()
        key = key + keyCharacter
    keyFile.close()
    path = pathlib.Path(filePath)
    file = open(path)
    string = ""
    fileCharacter = "place holder"
    while fileCharacter != "":
        fileCharacter = file.readline()
        string = string + fileCharacter
    file.close()
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
            cipher_text.append(string[counter])
            counter = counter + 1
        else:
            cipher_text.append(string[counter])
            counter = counter + 1
    encryptedString = ("".join(cipher_text))
    encryptedFilename = ""
    for character in filePath:
        if character == ".":
            encryptedFilename = encryptedFilename + "_end."
        else:
            encryptedFilename = encryptedFilename + character
    encryptedFile = open(encryptedFilename, "w")
    encryptedFile.write(encryptedString)
    encryptedFile.close()

# Decrypts the ciphertext
def originalText(filePath_decrypt, keyFile):
    key = ""
    keyCharacter = "place holder"
    while keyCharacter != "":
        keyCharacter = keyFile.readline()
        key = key + keyCharacter
    keyFile.close()
    pathDecrypt = pathlib.Path(filePath_decrypt)
    file = open(pathDecrypt)
    cipher = ""
    fileCharacter = "place holder"
    while fileCharacter != "":
        fileCharacter = file.readline()
        cipher = cipher + fileCharacter
    file.close()
    orig_text = []
    counter = 0
    keyCounter = 0
    while counter < len(cipher):
        if ord(cipher[counter]) in range(97, 123):
            x = (ord(cipher[counter]) - 96) - (ord(key[keyCounter]) - 96)
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
        elif ord(cipher[counter]) in range(65, 91):
            x = (ord(cipher[counter]) - 64) - (ord(key[keyCounter]) - 96)
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
        elif cipher[counter] == "\n" or cipher[counter] == "\t":
            orig_text.append(cipher[counter])
            counter = counter + 1
        else:
            orig_text.append(cipher[counter])
            counter = counter + 1
    decryptedString = ("".join(orig_text))
    decryptedFilename = filePath_decrypt.replace("_end", "_dec")
    decryptedFile = open(decryptedFilename, "w")
    decryptedFile.write(decryptedString)
    decryptedFile.close()


# Driver code
def main():
    print("Input a path to an HTML file: ")
    found = False
    while not found:
        try:
            filePath = input()
            pathTest = pathlib.Path(filePath)
            fileTest = open(pathTest)
            found = True
        except:
            print("Error, you entered an incorrect file path, please enter the correct path now: ")
    fileTest.close()
    print("Input an integer for how long you want the key to be: ")
    found = False
    while not found:
        try:
            keyLength = int(input())
            found = True
        except:
            print("Error, you did not enter an integer, please enter an integer this time: ")
    fileTest.close()
    key = generateKey(keyLength)
    keyFile = open("fileKey", "w")
    keyFile.write(key)
    keyFile.close()
    keyFile = open("fileKey", "r")
    cipher_text = cipherText(filePath, keyFile)
    print("Input the path to the encrypted HTML file for decryption: ")
    testFilename = ""
    for character in filePath:
        if character == ".":
            testFilename = testFilename + "_end."
        else:
            testFilename = testFilename + character
    found = False
    while not found:
        try:
            filePath_decrypt = input()
            if pathlib.Path(filePath_decrypt) == (pathlib.Path(testFilename)):
                pathTest = pathlib.Path(filePath_decrypt)
                fileTest = open(pathTest)
                found = True
            else:
                error = pathlib.Path("wrong_file")
                fileTest = open(error)
        except:
            print("Error, you did not enter the file that was previously encrypted, please do so now: ")
    fileTest.close()
    keyFile = open("fileKey", "r")
    origonal_text = originalText(filePath_decrypt, keyFile)
    keyFile.close()
main()