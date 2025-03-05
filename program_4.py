#Programmer: Timothy Pickering
#Date: 3/5/2025
#Title: Coordinate distance calc

#Required library
import math

#Coordinate distance math
def calculateDistance(point1, point2):
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

#User input
def getPointInput(pointNumber):
    while True:
        try:
            x, y, z = map(float, input(f"Enter the coordinates for point {pointNumber} (x, y, z) separated by spaces: ").split())
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter three numerical values separated by spaces.")

#Main program
print("3D Distance Calculator")

#User input for two points
point1 = getPointInput(1)
point2 = getPointInput(2)

#Pass input to function
distance = calculateDistance(point1, point2)

#Display result
print(f"The distance between {point1} and {point2} is: {distance:.2f}")
