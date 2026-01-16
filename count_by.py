def count_by(x, n):
        result = []
        for index in range(n):
                result.append(x*(index+1))
        print(result)

count_by(1, 5)#, [1, 2, 3, 4, 5])
count_by(2, 5)#, [2, 4, 6, 8, 10])
count_by(3, 5)#, [3, 6, 9, 12, 15])
count_by(50, 5)#, [50, 100, 150, 200, 250])
count_by(100, 5)#, [100, 200, 300, 400, 500])