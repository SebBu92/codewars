def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    for value in range(a, b + 1): # über alle zahlen iterieren
        text = str(value) # zahl in string wandeln
        ergebnis = 0 # ergebnis auf 0 setzen
        for index, zahl in enumerate(text): # über jeden index des string (ehemals zahl) iterieren
            ergebnis += (int(zahl) ** (index + 1)) # jeden wert in integer wandeln und mit index+1 als hochzahl und diese werte im ergebnis addieren
        if ergebnis == value:
            print(ergebnis)


sum_dig_pow(1, 135)#, [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]) 135 == 135 -> [0]**1 + [1] ** 2 + [2] ** 3