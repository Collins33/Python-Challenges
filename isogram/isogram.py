def is_isogram(string):
    #remove hyphen
    newString=string.replace("-","")
    #remove spaces
    newString.strip()
    #change the string into set
    newSet=set(newString)
    #change to lower
    newString.lower()


    if newString == "":
        return True
    elif len(newSet) != len(newString):
        return False
    elif len(newSet) == len(newString):
        return True   
