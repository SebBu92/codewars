def double_char(s):
    new_string = ""
    for value in s:
        new_string += (value * 2)
    print(new_string)

double_char("String")#,"SSttrriinngg")
double_char("Hello World")#,"HHeelllloo  WWoorrlldd")
double_char("1234!_ ")#,"11223344!!__  ")