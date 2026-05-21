def square_digits(num):
    ergebnis = ""
    for wert in str(num):
        x = (int(wert) * int(wert))
        ergebnis += str(x)
        print(x)
    print(ergebnis)


square_digits(9119)