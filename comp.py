def comp(array1, array2):
    a = []
    for value in array1:
        a.append(value ** 2)
        a.sort()
        array2.sort()
    print(a)
    print(array2)
    if a == array2:
        print(True)
    else:
        print(False)

array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
comp(array1, array2)#, True)