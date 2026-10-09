num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

operation = int(input("1: Addition\n2:subtracrion\n3: multiplication\n4:division\nEnter Operation:  "))

if operation == 1:
    print("Result: ",num1+num2)
elif operation == 2:
    print("Result: ",num1-num2)
elif operation == 3:
    print("Result: ",num1*num2)
elif operation == 4:
    print("Result: ",num1/num2)