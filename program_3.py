#Programmer: Timothy Pickering
#Date: 3/5/2025
#Title: US population by year

def collectData():
    #Initialize list
    dataList = []

    #Input loop
    while True:
        year = input("Enter the year (or type 'done' to stop): ")
        if year.lower() == 'done':
            break
        state = input("Enter the state name: ")
        population = input("Enter the population: ")

        #Convert inputs to appropriate types
        try:
            year = int(year)
            population = int(population)
            dataList.append([year, state, population])

        #Exception Handling
        except ValueError:
            print("Invalid input. Please enter numerical values for year and population.")

    #Add input to list
    return dataList

#Population math
def calculateTotalPopulation(dataList, targetYear):
    #Calculates the total population for a given year.
    totalPopulation = sum(entry[2] for entry in dataList if entry[0] == targetYear)
    return totalPopulation

#Main program
dataList = collectData()
targetYear = int(input("Enter a year to calculate total population: "))
totalPopulation = calculateTotalPopulation(dataList, targetYear)

print(f"The total population for the year {targetYear} is: {totalPopulation}")
