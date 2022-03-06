def test(n: int)->int:
    is_prime = True
    is_palindrom = False
    is_this_result = False
    n = n - 1
    while is_this_result == False:
        n = int(n)
        n += 1
        """
        Decide whether a number is prime or not.
        """
        is_prime = True

        if n < 2:
            is_prime = False
        if n == 2:
            is_prime = True
        if n % 2 == 0:
            is_prime = False

        i = 3
        maxi = n ** 0.5 + 1
        while i <= maxi:
            if n % i == 0:
                is_prime = False
            i += 2
        """
        Decide whether a string is palindrome or not
        """
        n = str(n)
        n2 = n[::-1]
        if n == n2:
            is_palindrom = True
        else:
            is_palindrom = False

        if is_prime and is_palindrom:
            is_this_result = True

    return n


def main():
    numbers: list[int] = [31, 130, 131, 1977]
    for i in range(len(numbers)):
        print("Tested:" + str(numbers[i]) + " and the result:" + str(test(numbers[i])))


if __name__ == '__main__':
    main()
