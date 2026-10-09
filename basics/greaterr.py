a = int(input("Enter A's Value "))
b = int(input("Enter B's Value "))
c = int(input("Enter C's Value "))
if a == b or a == c or b==c:
    print("two or more number are equal")
elif a>b and a > c:
    print("A is greatest")
elif b > c:
    print("B is greatest")
else:
    print("C is greatest")
    