import copy

def listToString(list: list[str]) -> str:
    if list == []:
        return ''
    
    newList = copy.copy(initialList)
    newList.insert(-1, 'and')
    newString = ''

    for index in range(len(newList) - 2):
        newList[index] += ','
    for index in range(len(newList)):
        newString += (newList[index] + ' ')

    
    print(initialList)
    print(newList)
    print(newString)

initialList = ['apples', 'bananas', 'tofu', 'cats']

listToString(initialList)

