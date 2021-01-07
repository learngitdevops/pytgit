#List Creation
#Finding the size of the list
'''
list1=[] #blank list
print("Elements of list1 :",list1)
print("Number of elements in list1 :",len(list1))

list2=[10,20,30]
print("Elements of list2 :",list2)
print("Number of elements in list2 :",len(list2))

list3=[10,20,"Python"]
print("Elements of list3 :",list3)
print("Position of the Elements in list3.")
print("1st Element of list3 at position[0] :",list3[0])
print("2nd Element of list3 at position[1] :",list3[1])
print("3rd Element of list3 at position[2] :",list3[2])
print("Number of elements in list3 :",len(list3))
'''
#Accessing Multidimensional List
list4=[[10,20,30],["Python","Java","C++"]]
print("Elements of list4 :",list4)
print("1st Element of list4 at position[0] :",list4[0])
print("2nd Element of list4 at position[1] :",list4[1])
print("Number of elements in list4 :",len(list4))
data1=list4[0][0]
data2=list4[1][2]
print("1st element of the 1st element :",data1)
print("3rd element of the 2nd element :",data2)