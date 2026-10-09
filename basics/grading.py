marks = int(input("Enter your marks: "))

if marks > 100 or marks <0:
    print("invalid Marks")
elif marks >= 90:
    print("Grade O")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks <= 45:
    print("You failed!")


    