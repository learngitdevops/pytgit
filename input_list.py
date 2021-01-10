#input() to find out the user specific element from the list
data=["10","python","30","java"]


rs=str(data)[1:-1]     #Converting the List to String
                       #Remove the 1st and lst character which is [ and ]   
new=rs.replace("'","") #Remove the single quotes
print("Current items :",new)

'''
s="-"
rs=s.join(data)
print("Current items :",rs)
'''

#Taking the input from user and convert that input to integer
list=input("Enter the position:")
conv=int(list)

#Using condition to check the range
if conv==0:
    print("Invalid Choice.")
    print("Please enter a number greater than 0 and smaller than 5.")
elif conv>4:
    print("Invalid Choice.")
    print("Please enter a number greater than 0 and smaller than 5.")
elif conv>0 and conv<=4:
    value=conv-1
    final=data[value]
    print("The value at position ",conv," is ",final)
