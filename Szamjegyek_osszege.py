def my_function(number, exponent):
    s_number = str(pow(number, exponent))
    sum = 0
    for i in s_number:
        sum += int(i)
    return sum


def main():
    i = 2
    j = 1000

    print("2^1000 számjegyeinek összege: ", my_function(i, j))


if __name__ == '__main__':
    main()
