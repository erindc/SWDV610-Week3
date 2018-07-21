# takes the last element in the list and then calls itself to shorten the list and take the last element again
#   until it reaches the end of the list
# appends the results of each call as a new list 

def reverseList(list):
    return [list[-1]] + reverseList(list[:-1]) if list else []

def main():
    listToRev = list(input('Enter a list to reverse: '))
    print(reverseList(listToRev))
          
main()