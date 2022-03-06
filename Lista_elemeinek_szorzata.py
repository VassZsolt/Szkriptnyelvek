def main():
    numbers = [1, 2, 3, 4, 5]
    print(product(numbers))


def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


if __name__ == '__main__':
    main()