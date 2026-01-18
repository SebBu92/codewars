def mine_location(field):
    mine_location = []
    for first_index, first_location in enumerate(field):
        for second_index,second_location in enumerate(first_location):
            if second_location == 1:
                mine_location.append(first_index)
                mine_location.append(second_index)
    return mine_location


mine_location([ [1, 0], [0, 0] ])#, [0, 0]
mine_location([ [1, 0, 0], [0, 0, 0], [0, 0, 0] ])#, [0, 0]
mine_location([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ])#, [2, 2]