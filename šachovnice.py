def chessboard(n):
    for radek in range(n):
        line(n, radek)

def line(n, radek):
    for sloupec in range(n):    
        check_position(radek,sloupec)
    print()
def check_position(radek,sloupec):
    if sloupec % 2 == radek % 2:
        print("#", end = " ")
    else:
        print(".", end = " ")

chessboard(8)