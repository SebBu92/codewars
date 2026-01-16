def two_sum(numbers, target):
    for index_1, value_1 in enumerate(numbers):
        for index_2, value_2 in enumerate(numbers):
            if  value_1 + value_2 == target and index_1 != index_2:
                print(index_1, index_2)

two_sum([1, 2, 3], 4)
two_sum([1234, 5678, 9012], 14690)
two_sum([2, 2, 3], 4)

    #   numbers       target   valid results
    # ([1 ,2, 3],            4,  ((0,2), (2,0))),
    # ([1234,5678,9012], 14690,  ((1,2), (2,1))),
    # ([2, 2, 3],            4,  ((0,1), (1,0))),
