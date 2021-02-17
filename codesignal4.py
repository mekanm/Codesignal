def adjacentElementsProduct(inputArray):
    list_one = []
    for x in range(len(inputArray)-1):
        multipe = inputArray[x] * inputArray[x+1]
        list_one.append(multipe)
    print(max(list_one))


adjacentElementsProduct([1,4,2,3,8,1,5])
