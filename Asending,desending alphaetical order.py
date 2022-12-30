'''print("Enter the String: ")
str = input()
str = sorted(str)
#str = sorted(str, reverse=True)
str = ''.join(str)
print("\nSorted String in ascending : ", str)
print("\nSorted String in Descending is: ",str)
#, end=""
'''

print("Enter the String: ", end="")
str = input()
str = sorted(str)
str = ''.join(str)
print("\nSorted String is:", str)
str = sorted(str, reverse=True)
str = ''.join(str)
print("\nSorted String in Descending is: ",str)
