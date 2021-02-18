def makeArrayConsecutive2(statues):
    list_of_missing = []
    for x in range(min(statues), max(statues)):
        if x in statues:
            pass
        else:
            list_of_missing.append(x)
    return len(list_of_missing)






