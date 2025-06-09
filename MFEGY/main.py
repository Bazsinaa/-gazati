import math
def main() -> None:
    print("MFEGY módszer, másodfokú egyenlet gyökei")
    a: int = int(input("Kérem az első számot: "))
    b: int = int(input("Kérem a második számot: "))
    c: int = int(input("Kérem a harmadik számot: "))
    x: float = 0
    x1: float = 0
    x2: float = 0
    if a != b:
        if b * b >= 4 * a * c:
            if b * b > 4 * a * c:
                print("Egy gyök!")
                x = -1 * (b / (2 * a))
                print(f"A megoldás: {x}")
            else:
                print("Két gyök!")
                x1 = (-1 * b + math.sqrt(b * b - 4 * a * c) ) / 2 * a
                x2 = (-1 * b - math.sqrt(b * b - 4 * a * c) ) / 2 * a
                print(f"A megoldások: {x1}, {x2}")
        else:
            print("Nincs valós gyök!")
    else:
        print("Nem másodfokú!")
        if b != 0:
            x = -1 * (c / b)
            print(f"A megoldás: {x}")
        else:
            if c != 0:
                print("Ellentmondás!")
            else:
                print("Azonosság!")

if __name__ == "__main__":
    main()
