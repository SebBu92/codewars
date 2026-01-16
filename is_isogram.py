def is_isogram(string):
    if len(string) == 0:
        return True
    string = string.lower()
    print(string)
    for x in string:
        zaehler = string.count(x)
        if zaehler >= 2:
            return False
    return True
    
is_isogram("Dermatoglyphics")#, True )
is_isogram("isogram")#, True )
is_isogram("aba")#, False, "same chars may not be adjacent" )
is_isogram("moOse")#, False, "same chars may not be same case" )
is_isogram("isIsogram")#, False )
is_isogram("")#, True, "an empty string is a valid isogram" )