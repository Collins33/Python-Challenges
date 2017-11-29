def is_isogram(string):
    if string == "":
        return True
    else:
        newString=string.replace("-","")
        newString.lower()
        count=0
        for x in range(0,len(newString)-1):
            for y in range(len(newString)-1,0,-1):

                if newString[x] == newString[y]:
                    count +=1

        if count == 1:
            return True
        else:
            return False
