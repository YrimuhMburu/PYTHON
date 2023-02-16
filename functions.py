vatRate = 12.5
#function declaration
print ("hello world")
def calculateTax(amount):
     tax = (amount * vatRate)/100
     totalAmount = amount + tax
     return totalAmount


userInput = int(input('Please enter amount : '))
bill = calculateTax(userInput)
print("Please pay this amount : " , bill)