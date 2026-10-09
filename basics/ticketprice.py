#under 12 10 per off     above 12 normal    
age = int(input("Enter Age: "))
role = input("Enter your role (Student or employee): ").lower()
ticket = 500
dis = 0
if age <= 12 or role == "student":
    dis = ticket/100*10
else:
    dis = 0
    
ticket = ticket - dis
print("Your ticket price is ", ticket)
