numberList = [0, 1, 12, 3, 14, 45, 76, 47, 18, 29, 10]
List1 = []
for num in numberList : 
    if num == 0 or num == 1 :
        continue
    for i in range(2, num // 2 + 1) :  
        if num % i == 0 :
            break
    else :   
        List1.append(num)
if len(List1) : 
    print("Prime Number : ",end = "-> ")
    for another in List1 :
        print(another, end = ", ") 
else :
    print("No any number from the given list is Prime")
