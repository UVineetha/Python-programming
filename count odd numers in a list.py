list1 = [10, 21, 44, 49, 78, 46]
count =0
for num in list1:
    if num % 2 != 0:
        count = count + 1
        print(num, end=" "  )
print("\n Number of odd numbers count : ",count)

