#Display user specific Index number value
data="PYTHON"
print("Base String is",data)
print("Total number of characters :",len(data)) #len() display total number of characters
print("0 is the 1st and -1 is the last character")
#input() to accept input from user
a=int(input("Enter the Index value:"))
b=data[a]
print("The character at ",a," position is :",b)


