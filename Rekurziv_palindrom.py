def rek_palindrom(s):
    if len(s) == 0:
        return s
    else:
        return rek_palindrom(s[1:]) + s[0]


def main():
    s = input("String:")
    if (s == rek_palindrom(s)):
        print("A megadott string Palindróm")
    else:
        print("A megadott string nem Palindróm")


if __name__ == '__main__':
    main()
