#capitalize() method takes no argument
#Capitalize the first character
data1="computer"
data2="language"
data3="python"
pdata=data1+' '+data2+' '+data3 #putting blank space between string 
print("Previous String :",pdata)
data4=data1.capitalize()
data5=data2.capitalize()
data6=data3.capitalize()
cdata=data4+' '+data5+' '+data6
print("Current String :",cdata)
print("------------------------------------------------")

#Convert the string to Uppercase
#upper() method takes no argument
print("Converting the string to Uppercase...")
a=pdata.upper()
print("Previous String :",pdata)
print("Current String :",a)
print("------------------------------------------------")

#Convert string to Lowercase
#lower() method takes no argument
print("Converting the string to Lowercase...")
b=a.lower()
print("Previous String :",a)
print("Current String :",b)


