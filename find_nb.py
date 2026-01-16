def find_nb(m):
    summe = 0
    zaehler = 1
    while summe < m:
        summe += zaehler ** 3
        zaehler += 1
    if summe == m:
        print(zaehler - 1)
    else:
        print(- 1)

find_nb(1071225)#, 45)
find_nb(4)#, -1)
find_nb(4183059834009)#, 2022)
find_nb(16)#, -1)
find_nb(24723578342962)#, -1)
find_nb(135440716410000)#, 4824)
find_nb(40539911473216)#, 3568)
find_nb(26825883955641)#, 3218)