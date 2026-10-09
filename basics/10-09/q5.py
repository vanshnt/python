# print the following pattern
    #     *
    #     ##
    #     ***
    #     ####
    
# n=5
n = int(input("Enter number of rows: "))

#loop to check the number of row and decides how many to print
for i in range(n+1):
    if i %2== 1:
        symbol = "*"
    else:
        symbol = "#"
    print(symbol*i)
    
