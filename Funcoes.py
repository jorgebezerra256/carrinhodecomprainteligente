def stringToListInt(string):
    listInt = []
    for c in string:
        listInt.append(ord(c))
    return listInt

def ListintToListString(inteiro):
    listChar = []
    for i in inteiro:
        listChar.append(chr(i))
    return listChar