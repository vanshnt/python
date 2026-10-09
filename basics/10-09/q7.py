# Add 2 nums at 3rd position on list and append one name in the list and split


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

#   checks if number is positive and insert sum on 3rd position 

if a> 0 and b>0:
    list.insert(2, a+b)
    print(list) 

# appends name

list.append("Vansh")
print(list)

#  splits from half

split = list.index(5)

left = list[:split]
right = list[split:]

print(f"Splited list\n{left}\n{right}")