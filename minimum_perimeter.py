# A rectangle can be defined by two factors: height and width.
# Its area is defined as the multiplication of the two: height * width.
# Its perimeter is the sum of its four edges: height + height + width + width.
# It is possible to create rectangles of the same area but different perimeters.
# For example, given an area of 45, the possible heights, widths and resultant perimeters would be:
# (1, 45) = 92
# (9, 5) = 28
# (15, 3) = 36
# Note that (6, 7.5) has an area of 45 too, but is discarded in this kata because its width is non integral.
# The task is to write a function that, given an area as a positive integer, returns the smallest perimeter possible of a rectangle with integral side lengths.
# Input range:
# 1 <= area <= 5 x 10 ^ 10

def minimum_perimeter(area):
    side_length = []
    for dividend in range(1, int(area**0.5)+1):
        if area % dividend == 0:
           side_length.append(dividend)
    print(int(2 * side_length[-1] + 2 * (area / side_length[-1])))



minimum_perimeter(45) #, 28
minimum_perimeter(30) #, 22
minimum_perimeter(81) #, 36
minimum_perimeter(89) #, 180

"""
Gegeben wird die Fläche und gesucht sind a und b die den kleinsten Umfang ergeben
Fläche = a*b
Umfang = 2*a + 2*b
Wenn Fläche = 45 dann ist eine Seitenlänge maximal 45 mm
45*1 = 45, 
"""