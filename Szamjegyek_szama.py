def main():
    Count_of_digits()


def Count_of_digits():
    number = 2**256
    s = str(number)
    print(f"2^256 contains {len(s)} digits")


if __name__ == '__main__':
    main()