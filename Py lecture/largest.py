arr = [3, 5, 99, 1, 6, 11]
max = arr[0]
min = arr[0]

print(arr)
for i in range(len(arr)):
    if max<=arr[i]:
        max = arr[i]
for i in range(len(arr)):
    if min>=arr[i]:
        min = arr[i]
        
print(f"maximum number in array is {max}")
print(f"Minumum number in array is {min}")