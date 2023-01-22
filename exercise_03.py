def getDict(s: str):
    s = s.lower()
    s = s.replace(' ', '')
    sDict: dict = {}

    for i in range(len(s)):
        sDict[s[i]] = s.count(s[i])

    return sDict


def main():
    strToIntDict = getDict(input("Enter a string: "))
    print(strToIntDict)
    return


main()
