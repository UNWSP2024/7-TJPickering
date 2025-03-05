#Programmer: Timothy Pickering
#Date: 3/4/2025
#Title: Greater than n

def displayGreaterNumbers(numberList, n):
    #Displays numbers in numList that are greater than n.
    for number in numberList:
        if number > n:
            #Display the list of numbers.
            print(f"List of numbers:", numberList)
            #Display the number.
            print("Threshold:", n)
            #Display the list of numbers that are larger than the number.
            print(number)

#Declare local variables
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5

#Call the main function.
displayGreaterNumbers(numberList, n)
