# 1. Sum of the first 10 positive even numbers

total = 0
for number in range(2, 21, 2):
    total += number

print(total)


# 2 accept two numbers s and n, print square of first n numbers starting from s 

s = int(input("Enter value of S: "))
n = int(input("Enter value of N: "))

for i in range(s,n+1):
    print(f"The square of {i} is {i ** 2}")