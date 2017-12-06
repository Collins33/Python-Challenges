def to_rna(dna_strand):
    dnaList=list(dna_strand)
    rnaList=[]


    for x in range(len(dnaList)):
        if dnaList[x] == "G":
            dnaList[x] = "C"
            rnaList.append(dnaList[x])
        elif dnaList[x] == "C":
            dnaList[x] = "G"
            rnaList.append(dnaList[x])
        elif dnaList[x] == "T":
            dnaList[x] = "A"
            rnaList.append(dnaList[x])
        elif dnaList[x] =="A":
            dnaList[x] = "U"
            rnaList.append(dnaList[x])
        else:
            raise ValueError

    str1=''.join(rnaList)
    return str1
to_rna("C")
