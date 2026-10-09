# create a heterogeneous list of numbers and name. split the list from the highest number

list = [30, "Vansh", 29, 84, "python", "java", 65]

#seprete and make and instance of the list with integers and max checks the max
high = max(value for value in list if isinstance(value, int))

#split the list at the position of the highest number
split = list.index(high)
left = list[:split]
right = list[split:]

print(left)
print(right)

