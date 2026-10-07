# create a list of 10 num and display the sum of last 4 elements
list = [8, 6, 4, 2, 99, 4, 12, 55, 78, 3]
last4sum= list[-4:]
print(list)
print(sum(last4sum))


# remove the items from the list located at 2nd and 5th position
print("removed 2nd and 5th position")
del list[1]
del list[4]
print(list)


# print the diff between highest and smallest number of list
list.sort()
print(list)
print("sum of highest and smallest is: ", list[0]+list[-1])

# append the new element in the list which is half of the item of 3rd position in the list
list.append(int(list[3]/2))
print(list)
