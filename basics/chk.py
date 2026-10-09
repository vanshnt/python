role =str(input("Enter your role (Student or Teacher):")).lower().strip()
age = int(input("enter age: "))
print(f"Eligibility: {role == "student" and age < 21}")