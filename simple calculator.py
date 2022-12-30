def mul(n1, n2):
    return n1 * n2
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1/ n2
v1 = int(input("Enter 1st number: "))
v2 = int(input("Enter 2nd number: "))
print("Select operation \n 1-Add \n 2-Sub \n 3-Multi \n 4-div \n")
choice = int(input("Choose 1/2/3/4: "))
if choice == 1:
    print(v1, "+", v2, "=", add(v1, v2))
elif choice == 2:
    print(v1, "-", v2, "=", sub(v1, v2))
elif choice == 3:
    print(v1, "*", v2, "=", mul(v1, v2))
elif choice == 4:
    print(v1, "/", v2, "=", div(v1, v2))
else:
   print("Enter correct operation")
