def median(numbers):
    temp = 0
    result = 0.000
    numbers.sort()
    if len(numbers) % 2 == 0:
        temp = int(len(numbers) / 2)
        result = (numbers[temp-1] + numbers[temp]) / 2
    else:
        import math
        temp = int(math.ceil(len(numbers) / 2))-1
        result = numbers[temp]

    return result


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    answer=median(numbers)
    print(answer)

if __name__ == '__main__':
    main()
