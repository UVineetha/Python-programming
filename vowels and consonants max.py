n=input("enter the string : ")
vowels=0
consonants=0
max(vowels,consonants)
for i in n:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
print("maximum is ",max(vowels,consonants))
if max(vowels,consonants)==consonants:
    print("maximum is consonants")
else:
    print("maximum is vowels")

