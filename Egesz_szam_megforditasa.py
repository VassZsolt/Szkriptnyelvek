def main():
    num = int(input("Number:"))
    num2 = Reverse_of_number(num)
    print(num2)


def Reverse_of_number(num):
    num = str(num)
    num2 = int(num[::-1])
    return num2


if __name__ == '__main__':
    main()
	