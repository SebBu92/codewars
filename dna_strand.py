def DNA_strand(dna):
    new_dna = ""
    for value in dna:
        if value == "A":
            new_dna += value.replace("A", "T")
        elif value == "T":
            new_dna += value.replace("T", "A")
        elif value == "C":
            new_dna += value.replace("C", "G")
        elif value == "G":
            new_dna += value.replace("G", "C")
        else:
            new_dna += value
    print(new_dna)

DNA_strand("AAAA")#, "TTTT"
DNA_strand("ATTGC")#,"TAACG","String ATTGC is")
DNA_strand("GTAT")#,"CATA","String GTAT is")