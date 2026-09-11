age = int(input("Enter Your Age: "))
weight = int(input("Enter your weight (kgs): "))

if age<18:
    if weight<50:
        print("You are healty")
    else:
        print("Not healthy")
if age<45:
    if weight<75:
        print("You are healthy")
    else:
        print("Not healthy")
else:
    print("Inalid input")