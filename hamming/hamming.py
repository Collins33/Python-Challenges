def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError
    elif len(strand_a) == len(strand_b):
        count=0
        firstList=list(strand_a)
        secondList=list(strand_b)

        for x in range(0,len(firstList)):
            #while firstList.index(firstList[x]) == secondList.index(secondList[x]):
            if firstList[x] != secondList[x]:
                count+=1
        return count



distance("GATACA", "GCATAA")
