def palindrom_1(s):
    if(s == s[::-1]):
        return True
    else:
        return False



def main():
    s = input("String:")
    is_this_palindrom = palindrom_1(s)
    if(is_this_palindrom==True):
        print("A megadott string Palindróm")
    else:
        print("A megadott string nem Palindróm")


if __name__ == '__main__':
    main()

