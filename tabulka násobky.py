def table_products(n):
    x = 0
    y = 0
    for i in range(n):
        x += 1
        print(x, end="  ")
    print()
    for i in range(n):
        print("-", end="  ")
    print()
    for i in range(1,n):
        y+=1
        print(y, end=" / ")
        for j in range(1,n+1):
            print(i*j,end=" ")
        print()






table_products(5)