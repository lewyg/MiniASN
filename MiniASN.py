from scanner.Scanner import Scanner


def main():
    scanner = Scanner('example.miniasn')
    t = scanner.get_token()
    while t:
        print(t)
        t = scanner.get_token()


if __name__ == "__main__":
    main()
