def word_count(phrase):
    phraseList=phrase.split()
    print(phraseList)
    countList=[]
    count=0
    for x in range(0,len(phraseList)):
        # for y in range(len(phraseList),0):
        if phraseList[x] == phraseList[x] and phraseList.index(phraseList[x]) != phraseList.index(phraseList[x]):
            count +=1

    print(count)



word_count('one fish two fish red fish blue fish')
