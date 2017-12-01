def is_pangram(sentence):
    sentence=sentence.lower()
    if sentence == "":
        return False
    else:
        letters="qwertyuiopasdfghjklzxcvbnm"
        letterList=list(letters)
        sentenceList=list(sentence)
        count =0
        for x in range(len(letterList)):
            if letterList[x] in sentenceList:
                count +=1

        if count == 26:
            return True
        else:
            return False
















is_pangram("The quick brown fo jumps over the lazy dog")
