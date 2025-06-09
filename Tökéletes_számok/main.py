def main() -> None:
    # Keresd meg és írd a képernyőre az első 4 tökéletes számot.
    osztok_osszege: int = 0
    esetek: int = 4
    print("Tökéletes számok:")
    n = 6
    while esetek != 0:
        osztok_osszege = 1
        szam = 2
        while szam <= n // 2:
            if n % szam == 0:
                osztok_osszege = osztok_osszege + szam
            szam = szam + 1
        if osztok_osszege == n:
            print(n)
            esetek -=1
        n = n + 1


if __name__ == "__main__":
    main()