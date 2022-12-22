string = "Python is a case sensitive language"
# Part A
print("The Length of the input String is ", len(string))

# Part B
string1 = string[::-1]
print("The Reversed String is: ", string1)

# Part C
string2 = string[10:26]
print("By using slicing function to store value: ", string2)

# Part D
string3 = string.replace("a case sensitive", "object oriented")
print("Replacing a case sensitive using replace function: ", string3)

# Part E
string5 = string.index("a")
print("The index of substring a is: ", string5),

# Part F(REMOVING WHITESPACES)
string4= string.strip()
print("Removing Whitespaces the string is: ", string4)