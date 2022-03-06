def Munchausen(n):
    li = [pow(i, i) for i in range(10)]  # created the appropriate powers
    li[0] = 0

    for number in range(n):
        snumber = str(number)
        sum = 0
        for i in snumber:
            sum += li[int(i)]
        if sum == number:  # compare the summaries and the numbers
            print(sum)


def main():
    n = 438579088 + 1  # the biggest Munchausen number+1 as limit in our function
    Munchausen(n)


if __name__ == '__main__':
    import time

    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
