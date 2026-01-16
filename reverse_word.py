def reverse_word(text):
        new_text = [] # neue leere Liste erstellen
        for word in text.split(" "): # bei leerzeichen wir gesplittet für einzelnen String und drüber iteriert
            new_text.append(word[::-1]) # jedes wort wird umgekehrt ([::-1]) und zur leeren liste hinzugefügt
        print(" ".join(new_text)) # jetzt gefüllte Liste mit einzelnen werten wird mit " " zusammengefügt

reverse_word('The quick brown fox jumps over the lazy dog.')