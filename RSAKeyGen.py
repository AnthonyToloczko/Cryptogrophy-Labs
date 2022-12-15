import time
import random

def primeNumber():
    table = ""
    binaryNumber = "1" # initializes binaryNumber with the starting bit that it should have
    counter = 5 # creates a counter for the while loop to get the needed 5 bits
    buffer = random.randint(1, 99)
    randomSeed = (time.time()) - buffer # uses time as the pseudorandom seed
    random.seed(randomSeed) # sets the seed of the built-in random generator to the new seed

    while counter > 0:
        randomNumber = bin(random.randint(0, 10000000000)) # chooses a random number between this range
        randomBit = randomNumber[len(randomNumber) - 1] # takes the least significant bit
        binaryNumber += randomBit # stores it with the other bits
        table += ("b_" + str(counter) + "|" + str(randomNumber).replace("0b", "") + "|" + str(randomBit) + "\n") # displays the trace
        counter -= 1 # updates the counter

    binaryNumber += "1" # gives the binary number the last bit that we know it must have
    regularNumber = int(binaryNumber, 2) # converts the binary to a regular number
    binaryNumber = "{:032b}".format(regularNumber) # turns the binary number from 7 bits into 32 bits (25 leading 0's)
    table = table + ("Number|" + str(regularNumber) + "|" + str(binaryNumber) +"\n") # displays the number and it's trace
    return regularNumber, table

def primalityTest(x, n):
    e = n - 1
    y = x
    table = ("\n" + "p=" + str(n) + ", a=" + str(x) + "\n")
    table = table + ("i |\txᵢ\t|\tz\t|\ty\t|\ty\n")
    table = table + "__|_____________|_______________|_______________|_____________\n"
    table = table + ("0 |\t1\t|\t1\t|\t1\t|\t" + str(x) + "\n")
    for i in range(1, len(bin(e)[2:])):
        z = y
        y = (y * y) % n
        if y == 1 and z != 1 and z != e:
            table += (str(i) + " |\t" + bin(e)[2:][i] + " \t|\t" + str(z) + "\t|\t" + str(y) + "\t|\t" + str((y * x) % n) + "\n")
            table += (str(n) + " is not prime\n")
            return False, table
        if int(bin(e)[2:][i]) == 1:
            table += (str(i) + " |\t" + bin(e)[2:][i] + " \t|\t" + str(z) + "\t|\t" + str(y) + "\t|\t" + str((y * x) % n) + "\n")
            y = (y * x) % n
        else:
            table += (str(i) + " |\t" + bin(e)[2:][i] + " \t|\t" + str(z) + "\t|\t" + str(y) + "\t|\t" + str(y) + "\n")
    if y != 1:
        table += ("\n" + str(n) + " is not prime\n")
        return False, table
    else:
        table += ("\n" + str(n) + " is perhaps prime\n")
        return True, table

def extendedEuclid(m, n):
    table = ("i |\tqᵢ\t|\tr\t|\trᵢ+1\t|\trᵢ+2\t|\tsᵢ\t|\ttᵢ\n")
    table += ("__|_____________|_______________|_______________|_______________|_______________|_______________\n")
    i = 1
    s = [] 
    t = [] 
    qNumbers = []
    if m < n:
            nSwap = m
            m = n
            n = nSwap
    mod = m
    while n != 0:
        q = int(m / n)
        qNumbers.append(q)
        if i == 1:
            s.append(1), t.append(0)
        elif i == 2:
            s.append(0), t.append(1)
        else:
            s.append(s[i-3]-(qNumbers[i-3]*s[i-2])), t.append(t[i-3]-(qNumbers[i-3]*t[i-2]))
        r = m % n
        table += (str(i) + " |\t" + str(q) + "\t|\t" + str(m) + "\t|\t" + str(n) + "\t|\t" + str(r) + "\t|\t" + str(s[i-1]) + "\t|\t" + str(t[i-1]) + "\n")
        m = n
        n = r
        i += 1
    s.append(s[i-3]-(qNumbers[i-3]*s[i-2])), t.append(t[i-3]-(qNumbers[i-3]*t[i-2]))
    q = ""
    n = ""
    r = ""
    table += (str(i) + " |\t" + str(q) + "\t|\t" + str(m) + "\t|\t" + str(n) + "\t|\t" + str(r) + "\t|\t" + str(s[i-1]) + "\t|\t" + str(t[i-1]) + "\n")
    if t[i-1] < 0:
        t[i-1] = t[i-1] + mod
    print(table)
    return t[i-1], m

def main():
    counter = 0
    p = primeNumber()
    traces = p[1]
    p = p[0]
    q = primeNumber()
    q = q[0]
    while counter < 20:
        randomNumber = random.randint(1, 127)
        while randomNumber >= p or randomNumber >= q:
            randomNumber = random.randint(1, 127)
        firstResult = primalityTest(randomNumber, p)
        secondResult = primalityTest(randomNumber, q)
        if firstResult[0] is False:
            p = primeNumber()
            traces = p[1]
            p = p[0]
            counter = -1
        if secondResult[0] is False:
            q = primeNumber()
            q = q[0]
            counter = -1
        counter += 1
    traces += firstResult[1]
    randomNumber = random.randint(1, 44)
    nonPrimeProof = primalityTest(randomNumber, 44)
    traces += nonPrimeProof[1]
    e = 3
    n = p*q
    traces += "\ne = " + str(e) + "\n"
    print(traces)
    euclid = extendedEuclid(e, n)
    d = euclid[0]
    while (euclid[1] % n) != 1:
        e += 1
        print("e = " + str(e) + "\n")
        euclid = extendedEuclid(e, n)
        d = euclid[0]
    print("d = " + str(d) + "\n")
    print("p = " + str(p) + ", q = " + str(q) + ", n = " + str(n) + ", e = " + str(e) + ", d = " + str(d))
    print("{:032b}".format(p))
    print("{:032b}".format(q))
    print("{:032b}".format(n))
    print("{:032b}".format(e))
    print("{:032b}".format(d))

main()