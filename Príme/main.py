def osztók_száma(vszám: int) -> bool:
    db: int = 0
    for osztó in range(1, vszám + 1):
        if vszám % osztó == 0:
            db += 1
    return db == 2

def main() -> None:

    szám: int = int(input("Kérem a vizsgált számot: "))
    print(f"A szám {"" if osztók_száma(szám) else "nem "}prímszám")


if __name__ == "__main__":
    main()
