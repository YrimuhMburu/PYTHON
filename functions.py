import os
vatRate = 12.5
#function declaration
print ("hello world")
def calculateTax(amount):
     tax = (amount * vatRate)/100
     totalAmount = amount + tax
     return totalAmount


def readFile():
     #print("this is the beginning of file handling process")
     file = open("file.txt", "r")
     print(file.read())
     file.close()
     #how to deal with except 
def writeFile(totalAmount):
    try:
         file1 = open("file1.txt", "w")
         file1.write("Total amount for this customer is {0} " .format(totalAmount) )#method 1
         file1.close()
    except file1.exception:
         print("there is an error in this file ")
def currentWorkingDirectory():
    cwd = os.getcwd()
    cwd = os.getlogin()
    print(cwd)
         #two methods to write the total amount to file1.txt
         #(method 2)file1.write("Total amount for this customer is "+ str(totalAmount) )