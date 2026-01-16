def frame(score):
    score_without_clamp = "" # leerer string für neue score werte ohne klammer
    inside_clamp = False # default wert ist False
    player_1 = 0
    player_2 = 0
    for char in score: # pber string iterieren
        if char == "(": # bei öffnender klammer auf true setzen
            inside_clamp = True
            continue
        if char == ")": # bei schließender klammer auf False setzen
            inside_clamp = False
            continue
        if not inside_clamp: # wenn False dann zeichen un leeren string hinzufügen
            score_without_clamp += char
# jetzt habe ich einen neuen string ohne klammern
    frame_score = score_without_clamp.split("; ")
# jetzt habe ich eine Liste wor jeder index ein string mit dem fram ergebnis ist
    for scores in frame_score: # ich iteriere über die neue Liste
        single_frame_score = scores.split("-") # wieder neue Liste ohne bindestrich
# jetzt habe ich eine Liste wo jedes ergebnis ein eigener string ist
        if int(single_frame_score[0]) > int(single_frame_score[1]): # in integer wandeln
            player_1 += 1
        else:
            player_2 += 1
    print([player_1, player_2])


score = "24-79(72); 16-101(53); 86(58)-27; 31-90(74); 0-115(115); 67-40; 61-21; 81(55)-23; 51-14; 124(56,68)-4; 67-12; 108(85)-15; 1-117(117); 1-92(92); 130(112)-0; 1-106(53); 59-39"
frame(score) #[10,7]