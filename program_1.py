#Programmer: Timothy Pickering
#Date: 3/4/2025
#Title: Rainfall Calc

#Initialize an empty list to store rainfall amounts
rainfallList = []

#Loop to get rainfall data for each of the 12 months
for count in range(12):
    monthlyRainfall = float(input(f"Enter rainfall for month {count+1}: "))
    rainfallList.append(monthlyRainfall)

#Calculate total and average rainfall
totalRainfall = sum(rainfallList)
averageRainfall = totalRainfall / 12

#Find the highest and lowest rainfall amounts and their corresponding months
maxRainfall = max(rainfallList)
minRainfall = min(rainfallList)
maxMonth = rainfallList.index(maxRainfall) + 1  #Adding 1 to match month number
minMonth = rainfallList.index(minRainfall) + 1

#Display results
print("Rainfall Report:")
print(f"Total rainfall for the year: {totalRainfall:.2f} inches")
print(f"Average monthly rainfall: {averageRainfall:.2f} inches")
print(f"Month {maxMonth} had the highest rainfall: {maxRainfall:.2f} inches")
print(f"Month {minMonth} had the lowest rainfall: {minRainfall:.2f} inches")
