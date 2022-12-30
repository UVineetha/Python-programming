def reverse_string(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
str="MOSQUE"
print("the word alphabetically string is:",str)
print("the reverse string",reverse_string(str))
