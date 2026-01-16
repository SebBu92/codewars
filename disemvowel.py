def disemvowel(string):
    vokale = "aeiouAEIOU"
    neuer_string = []
    for buchstabe in string:
        if buchstabe not in vokale:
            neuer_string.append(buchstabe)
    return ("".join(neuer_string))
        
    
disemvowel("This website is for losers LOL!")