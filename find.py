#find() returns the index number of the 1st occurence of the given character.
# and also used to return the index number of the 1st occurence of the word from where it starts
data="python is a computer language. java is also a computer language."
a=data.find("t") #1st occurence of a single character
print("1st occurence of 't' :",a)
a=data.find("computer") #1st occurence of a word or string
print("1st occurence of 'computer' starts from :",a)
