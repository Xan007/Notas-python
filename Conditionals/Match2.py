point = (0,0)

#TUPLAS
match point:
    case (x, y) if x == 0 and y == 0:
        print("En el centro")
    case (0, y):
        print("En el eje Y")
    case (x, 0):
        print("En el eje X")
    case (x, y):
        print("En ningun eje")