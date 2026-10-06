# n = int(input("Enter Number"))
# for i in range(n+1):
#     for j in range(i+1):
#         print(j, end = " ")
#     print()
    
# n = int(input("Enter Number"))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end = " ")
#     print()
    

# n = 5

# for i in range(1, n + 1):
#     for sp in range(n - i):
#         print(" ", end=" ")

#     for j in range(1, i + 1):
#         print(j, end=" ")

#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")

#     print()
    
        
# n = 5
# for i in range(n):
#     print(" " * (n - i - 1), end="")
#     for j in range(2 * i + 1):
#         print(chr(65 + j), end=" ")
#     print()



n = 5
for i in range (n):
    print(" " *(n-i+1), end ="")
    for j in range(2*i+1):
        if(j==0 or j ==2*i or i==n-1):
            print(chr(65+j), end = " ")
        else:
            print(" ", end = " ")
    print()
    