def hey(phrase):
    #check if it is empty
    newPhrase=phrase.replace("          ","")
    secondPhrase=phrase.replace("\t","").replace("\n","").replace("\r","")
    if phrase == "":
        return 'Fine. Be that way!'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase.strip().endswith("?"):
        return 'Sure.'
    elif newPhrase=="":
        return 'Fine. Be that way!'
    elif secondPhrase=="":
        return 'Fine. Be that way!'

    else:
        return 'Whatever.'








hey("\t\t\t\t\t\t\t\t\t\thello")
