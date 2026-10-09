# Print a centered star pyramid.
n = int(input("Enter no of lines: "))

for i in range(n):
    #add spaces befor printing *
    #1 space reduces in each loop
    spaces =n-i-1
    # adds stars
    # 2 stars gets added after 1st loop for each loop
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)
    