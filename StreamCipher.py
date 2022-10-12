import random
import time

def keyGenerator(string, seed):
    random.seed(seed)
    byteArrayKey = random.randbytes(len(string))
    return byteArrayKey

def Encryptor(string, seed):
    byteArrayKey = keyGenerator(string, seed)
    encodedString = string.encode()
    encodedByte = bytes(encodedString)
    counter = 0
    encryptedItem = 0
    encryptedList = list("")
    while counter < len(encodedString):
        encryptedItem = (encodedByte[counter]^byteArrayKey[counter])
        encryptedList.append(encryptedItem)
        counter += 1
    encryptedList = bytes(encryptedList)
    return encryptedList

def Decryptor(encryptedString, seed):
    byteArrayKey = keyGenerator(encryptedString, seed)
    encryptedList = encryptedString
    counter = 0
    decryptedItem = 0
    decryptedList = list("")
    while counter < len(encryptedString):
        decryptedItem = (encryptedList[counter]^byteArrayKey[counter])
        decryptedList.append(decryptedItem)
        counter += 1
    decryptedList = bytes(decryptedList)
    decryptedList = decryptedList.decode()
    return decryptedList

def main():
    randomSeed = int(time.time())
    print("Enter a string that you want to encrypt: ")
    plaintext = input()
    print("Random seed: ", int(randomSeed))
    print("Input string: ", plaintext)
    
    print("Psuedo random sequence: ", keyGenerator(plaintext, randomSeed))
    # Not required for the rest of the functions within the program to run, it is just here since the example
    # had this as a part of the output
    
    encryptedPlaintext = Encryptor(plaintext, randomSeed)
    print("Output byte: ", encryptedPlaintext)
    print("The decrypted string: ", Decryptor(encryptedPlaintext, randomSeed))
main()