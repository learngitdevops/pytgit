#Check whether the string starts or ends with a specific value
#Returns result "True" or "False"
#startswith(value,start_position,end_position)
data="Python is a computer progranmming language"
sw=data.startswith("Python")
print("Starts with Python :",sw)
sw=data.startswith("python")
print("Starts with 'python' :",sw)
sw=data.startswith("computer")
print("Starts with 'computer' :",sw)
sw=data.startswith("ter",17,25) # Search within a range
print("Starts with 'ter' :",sw)
print("---------------------------------")
ew=data.endswith("language")
print("Ends with 'language' :",ew)
ew=data.endswith("computer")
print("Ends with 'computer' :",ew)
ew=data.endswith("a",6,11) # Search within a range
print("Ends with 'a' :",ew)


