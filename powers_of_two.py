# def powers_of_two(n):
#     result = []
#     multiplier = 0
#     while multiplier <= n:
#         result.append(2 ** multiplier)
#         multiplier += 1
#     print(result)

def powers_of_two(n):
    result = []
    for value in range(0, n+1):
        result.append(2 ** value)
    print(result)

powers_of_two(0)#, [1])
powers_of_two(1)#, [1, 2])
powers_of_two(4)#, [1, 2, 4, 8, 16])



