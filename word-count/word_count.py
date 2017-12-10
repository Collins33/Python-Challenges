def word_count(phrase):
    newPhrase=phrase.replace(":","").replace(".","").replace("_"," ").replace(","," ")
    phraseList=newPhrase.lower().split()
    print(newPhrase)
    countList=[]
    countDict={}

    for x in range(0,len(phraseList)):
        countList.append(phraseList.count(phraseList[x]))
        countDict[phraseList[x]]=countList[x]

    print(countList)
    return countDict




word_count('First: don\'t laugh. Then: don\'t cry.')
