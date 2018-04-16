def string_length(mystring):
    return len(mystring)


mine = input("enter a string to get the length of: ")

print type(mine)

if type(mine) != "String":
    print("you must enter a string")
else:
    print(string_length(mine))
