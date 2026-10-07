name = input("Enter your name").lower()

a = "a"
count = 0
for i in name:
    if i in a:
        count+=1
        
print("Count: ", count)