def expMod(x, e, n):
    y = x
    print("  | \tSquaring\t Multiplying")
    print("i | xᵢ\ty\t\t y")
    print("__|____________________________________________")
    print("0 | " + bin(e)[2:][0] + "\t\t\t " + str(x))
    for i in range(1, len(bin(e)[2:])):
        tableY = y
        y = (y * y) % n
        if int(bin(e)[2:][i]) == 1:
            print(str(i) + " | " + bin(e)[2:][i] + "\t" + str(tableY) + "² mod " + str(n) + " = " + str(y) + "\t " + str(x) + " x " + str(y) + " mod " + str(n) + " = " + str((y * x) % n))
            y = (y * x) % n
        else:
             print(str(i) + " | " + bin(e)[2:][i] + "\t" + str(tableY) + "² mod " + str(n) + " = " + str(y) + "\t " + str(y))
    return y