def divisors(n):
    anzahl_divisors = 0
    for x in range(1,n+1):
        if n % x == 0:
            anzahl_divisors += 1
    print(anzahl_divisors)


divisors(5)#, 2)
divisors(4)#, 3)
divisors(1)#, 1)
divisors(12)#, 6)
divisors(30)#, 8)
divisors(4096)#, 13)