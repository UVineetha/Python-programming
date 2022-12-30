n=input("enter a string : ")
rev = n[::-1]
if n == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")

"""def pal(input_str):
    for i in range(0,len(input_str)):
     if input[i]!=input[len(input_str)-i-1]:
       return false
 return true
#i=input("enter a string : ")
#input_str = "civic"
print("Palindrome") if isPalindrome(input_str) else print("Not Palindrome")
"""
