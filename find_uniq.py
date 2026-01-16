from collections import Counter
def find_uniq(arr):
    counts = Counter(arr)
    for number, counter in counts.items():
        if counter == 1:
            print(number)


find_uniq([ 1, 1, 1, 2, 1, 1 ])#, 2)
find_uniq([ 0, 0, 0.55, 0, 0 ])#, 0.55)
find_uniq([ 3, 10, 3, 3, 3 ])#, 10)