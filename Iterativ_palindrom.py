def iterativ_palindrom(s):
    is_this_palindrome = True
    i = len(s) - 1
    j = 0
    while i > 0:
        if (s[i] != s[j]):
            is_this_palindrome = False
        i -= 1
        j += 1

    return is_this_palindrome


def main():
    s = input("String:")
    if (iterativ_palindrom(s)):
        print("A megadott string Palindróm")
    else:
        print("A megadott string nem Palindróm")


if __name__ == '__main__':
    main()
