def main() -> None:
    print("LNKO kivonásos módszerrel")
    a: int = int(input("Kérem az egyik számot: "))
    b: int = int(input("Kérem a másik számot: "))
    print(f"LNKO({a},{b}) = ", end="")
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    # print(f"A két szám legnagyobb közös osztója: {a}")
    print(a)  # vagy print(b), mivel a == b



if __name__ == "__main__":
    main()
