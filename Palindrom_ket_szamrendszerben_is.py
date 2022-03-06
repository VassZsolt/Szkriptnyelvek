def binary_converter(n: str)->str:
    temp = str(bin(int(n)))
    b=""
    for i in range(2, len(temp)):
        b += str(temp[i])
    return b

def test()->int:
    numbers=[]

    for number in range(1000000):
        """
        Decide whether a string is palindrome or not
        """
        n = str(number)
        n2 = n[::-1]
        if n == n2:
            is_palindrom = True
        else:
            is_palindrom = False

        is_palindrom_in_binary=False
        b=binary_converter(n)

        """
        Decide whether a string is palindrome or not
        """
        b2 = b[::-1]
        if b == b2:
            is_palindrom_in_binary = True
        else:
            is_palindrom_in_binary = False

        if is_palindrom and is_palindrom_in_binary:
            numbers.append(number)
    sum=0
    for i in numbers:
        sum+=i

    return sum


def main():
    print("The result is: "+str(test()))

if __name__ == '__main__':
    main()
