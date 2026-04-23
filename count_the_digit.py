def nb_dig(n, d):
    counter = 0
    for k in range(0, n+1):
        square = k**2
        # print(f"Square: {square}")
        for digit in str(square):
            if digit == str(d):
                counter += 1
                # print(f"Counter: {counter}")
    print(counter)

nb_dig(25, 1)#, 11)
nb_dig(5750, 0)#, 4700)
nb_dig(11011, 2)#, 9481)
nb_dig(12224, 8)#, 7733)
nb_dig(11549, 1)#, 11905)
nb_dig(14550, 7)#, 8014)
nb_dig(8304, 7)#, 3927)
nb_dig(10576, 9)#, 7860)
nb_dig(12526, 1)#, 13558)
nb_dig(7856, 4)#, 7132)
nb_dig(14956, 1)#, 17267)
