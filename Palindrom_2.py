def palindrom_2(s):
    s2 = ""
    for i in s:
        s2 = i+s2
    return s2


def main():
    s=input("String:")
    answ_2=palindrom_2(s)
    if(s==answ_2):
        print("A megadott string Palindróm")
    else:
        print("A megadott string nem Palindróm")


if __name__ == '__main__':
    main()