def main() -> None:
    print("Szám faktoriálisa")
    # 5! = 1 * 2 * 3 * 4 * 5 = 120
    n: int = int(input("n = "))
    faktoriális: int = 1
    for i in range(2, n + 1):
        faktoriális = faktoriális * i
    print(f"{n}! = {faktoriális}")

if __name__ == "__main__":
    main()
