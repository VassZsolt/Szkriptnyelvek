import sys


def main():
    sum1()

def sum1():
    number1 = 0
    number2 = 0

    if(len(sys.argv)==3):
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
        print(number1 + number2)
    else:
        print("Insufficient number of inputs")


if __name__ == '__main__':
    main()