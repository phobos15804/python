def chessboard(n):
    for i in range(n):
        if i % 2 == 0:
            even_line(n)
        else:
            odd_line(n)


def even_line(n):
    for j in range(n):
        if j % 2 == 0:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()


def odd_line(n):
    for j in range(n):
        if j % 2 == 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()


chessboard(8)
