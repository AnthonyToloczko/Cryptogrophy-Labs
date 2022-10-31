def gcd(m, n):
    print("i |\tq\tm\tn\tr")
    print("_______________________________________________________")
    i = 0
    if m < n:
            nSwap = m
            m = n
            n = nSwap
    while n != 0:
        r = m % n
        q = int(m / n)
        print(str(i) + " |\t" + str(q) + "\t" + str(m) + "\t" + str(n) + "\t" + str(r))
        m = n
        n = r
        i += 1
    q = ""
    r = "STOP"
    print(str(i) + " |\t" + q + "\t" + str(m) + "\t" + str(n) + "\t" + str(r))
    return m

def main():
    print("Enter the value you would like m to be: ")
    number = False
    while not number:
        try:
            m = int(input())
            number = True
        except:
            print("You did not enter a number, please do so now: ")
    print("Enter the value you would like n to be: ")
    number = False
    while not number:
        try:
            n = int(input())
            number = True
        except:
            print("You did not enter a number, please do so now: ")
    print("")
    gcd(m, n)
main()
