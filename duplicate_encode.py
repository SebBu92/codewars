def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    for letter in word:
        counter =  word.count(letter)
        if counter == 1:
            new_word += "("
        else:
            new_word += ")"
    print(new_word)

duplicate_encode("din")
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")