def minAndMax(numList):
    if len(numList) == 1:
        return [numList[0], numList[0]]   # return as min & max
    else:
        mid = len(numList) // 2
        firstHalfRes = minAndMax(numList[:mid])  # find min and max of first half of list
        secondHalfRes = minAndMax(numList[mid:]) # find min and max for second half of list
        
        # figure out the min between the two lists
        if (secondHalfRes[0] < firstHalfRes[0]):
            firstHalfRes[0] = secondHalfRes[0]
            
        # figure out the max between the two lists
        if (secondHalfRes[1] > firstHalfRes[1]):
            firstHalfRes[1] = secondHalfRes[1]
            
        return firstHalfRes
    
def main():
    numList = input("Please enter a list of at least 2 numbers: ")
    numList = numList.split(',')
    numList = list(map(int, numList))
    
    min, max = minAndMax(numList)
    print('The min is: ', min, 'And the max is: ', max)

main()
    
