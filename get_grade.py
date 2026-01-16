def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if average > 89:
        print("A")
    elif average < 79:
        print("B")
    elif average < 69:
        print("C")
    elif average < 59:
        print("D")
    else:
        print("F")

get_grade(95, 90, 93)#, "A", "get_grade(95, 90, 93)")
get_grade(100, 85, 96)#, "A", "get_grade(100, 85, 96)")
get_grade(92, 93, 94)#, "A", "get_grade(92, 93, 94)")
get_grade(100, 100, 100)#, "A", "get_grade(100, 100, 100)")