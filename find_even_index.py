def find_even_index(arr):
    for index, value in enumerate(arr): # for schleife über jede stelle der liste mit ermittlung des index
        if (sum(arr[:index])) == (sum(arr[(index + 1):])): # slice von 0 bis index (index exklusive) und von index+1 bis ende
            print(index) #index ausgeben wenn die hälften == sind
            return
    print(-1) # wenn ungleich dann -1 ausgeben

find_even_index([1,2,3,4,3,2,1])#,3)
find_even_index([1,100,50,-51,1,1])#,1,)
find_even_index([1,2,3,4,5,6])#,-1)
find_even_index([20,10,30,10,10,15,35])#,3)
find_even_index([20,10,-80,10,10,15,35])#,0)
find_even_index([10,-80,10,10,15,35,20])#,6)
find_even_index(list(range(1,100)))#,-1)
find_even_index([0,0,0,0,0])#,0