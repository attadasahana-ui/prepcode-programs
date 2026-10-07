rows = 6
for j in range(1, rows + 1):
    for k in range(rows - j):
        print(" ", end="")

    for i in range(j):
         print("*",end=" ")

    print() 