#print odd number from one to 10

print("\n____Step method____")
for i in range(1, 10, 2):
    print(i, end = " ")

print("\n____condition method____")

for i in range(10):
    if i%2!=0:
        print(i, end =" ")