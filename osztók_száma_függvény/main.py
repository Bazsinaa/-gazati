def osztók_száma(szám: int) -> int:
    db: int = 0
    for osztó in range(1, szám + 1):
        if szám % osztó == 0:
            db += 1
    return db

def main() -> None:
    print("Osztók számának meghatározása")
    print("Adj meg két szélső értéket!")
    tól: int = 0
    ig: int = 0
    while ig - tól < 5:
        tól = int(input("tól ="))
        ig = int(input("ig ="))
        if ig - tól < 5:
            print("Az ig-tól>=5 feltétel nem teljesül!")
    osztók_száma_összesen: int = 0
    for vizsgált_szám in range(tól, ig + 1):
        osz: int = osztók_száma(vizsgált_szám)
        osztók_száma_összesen += osz
        print(f"{vizsgált_szám} -> Osztók száma: {osz}db")
    print(f"Osztók száma összesen: {osztók_száma_összesen}db")


if __name__ == "__main__":
    main()
