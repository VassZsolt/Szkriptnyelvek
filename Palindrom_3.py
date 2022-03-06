def palindrom_3(s):
    if len(s) == 0:
        return s
    else:
        return palindrom_3(s[1:]) + s[0]


def main():
    s=input("String:")
    answ_3 = palindrom_3(s)
    if(s==answ_3):
        print("A megadott string Palindróm")
    else:
        print("A megadott string nem Palindróm")

if __name__ == '__main__':
    main()