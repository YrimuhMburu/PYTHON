from functions import calculateTax,  readFile, writeFile, currentWorkingDirectory
import math



userInput = int(input('Please enter amount : '))
bill = calculateTax(userInput)
print("Please pay this amount : " , bill)
print("This is the floored bill" , math.floor(bill))
readFile()
writeFile(bill)
currentWorkingDirectory()