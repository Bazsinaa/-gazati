def main() -> None:
    print("Legkisebb közös többszörös")
    a: int = int(input("Kérem az első számot: "))
    b: int = int(input("Kérem a második számot: "))
    lkkt: int = 1

    while lkkt % a != 0 or lkkt % b != 0:
        lkkt = lkkt + 1

    if lkkt % a == 0 and lkkt % b == 0:
        print(f"A legkisebb közös többszörös: {lkkt}")


if __name__ == "__main__":
    main()
