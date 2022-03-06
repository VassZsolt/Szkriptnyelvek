def f1():
    input = ['auto', 'villamos', 'metro']
    output = [n.upper() + "!" for n in input]

    print("F1:")
    for n in input:
        print("\"" + n + "\"", end=" ")
    print()

    for n in output:
        print("\"" + n + "\"", end=" ")
    print("\n")


def f2():
    input = ['aladar', 'bela', 'cecil']
    output = [n.capitalize() for n in input]

    print("F2:")
    for n in input:
        print("\"" + n + "\"", end=" ")
    print()

    for n in output:
        print("\"" + n + "\"", end=" ")
    print("\n")


def f3():
    output = ["0" for i in range(10)]

    print("F3:")
    for n in output:
        print(n, end=" ")
    print("\n")


def f4():
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    output = [n * 2 for n in input]

    print("F4:")
    for n in input:
        print(n, end=" ")
    print()

    for n in output:
        print(n, end=" ")
    print("\n")


def f5():
    input = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    output = [int(n) for n in input]

    print("F5:")
    for n in input:
        print('\'' + n + '\'', end=" ")
    print()

    for n in output:
        print(n, end=" ")
    print("\n")


def f6():
    input = "1234567"
    output = [int(n) for n in input]

    print("F6:")
    print("\"" + input + "\"")

    for n in output:
        print(n, end=" ")
    print("\n")


def f7():
    input = 'The quick brown fox jumps over the lazy dog'
    input2 = []
    input2 = input.split()
    output = [len(n) for n in input2]

    print("F7:")
    print("\"" + input + "\"")

    for n in input2:
        print("\"" + n + "\"", end=" ")
    print()

    for n in output:
        print(n, end=" ")
    print("\n")


def f8():
    input = "python is an awesome language"
    input2 = []
    input2 = input.split()
    output = [n[0] for n in input2]

    print("F8:")
    print("\"" + input + "\"")

    for n in input2:
        print("\"" + n + "\"", end=" ")
    print()

    for n in output:
        print("\'" + n + "\'", end=" ")
    print("\n")


def f9():
    input = 'The quick brown fox jumps over the lazy dog'
    input2 = []
    input2 = input.split()
    output = [n + " " + str(len(n)) for n in input2]

    print("F9:")
    print("\"" + input + "\"")

    for n in input2:
        print("\"" + n + "\"", end=" ")
    print()

    for n in output:
        print("\'" + n + "\'", end=" ")
    print("\n")


def f10():
    output = [i for i in range(10) if i % 2 == 0]

    print("F10:")
    for n in output:
        print(n, end=" ")
    print("\n")


def f11():
    input = [i for i in range(20)]
    input2 = [i * i for i in input]
    output = [i for i in input2 if i % 2 == 0]

    print("F11:")
    for n in input:
        print(n, end=" ")
    print()

    for n in input2:
        print(n, end=" ")
    print()

    for n in output:
        print(n, end=" ")
    print("\n")


def f12():
    input = [i for i in range(20)]
    input2 = [i * i for i in input]
    output = [i for i in input2 if str(i)[len(str(i)) - 1] == '4']

    print("F12:")
    for n in input:
        print(n, end=" ")
    print()

    for n in input2:
        print(n, end=" ")
    print()

    for n in output:
        print(n, end=" ")
    print("\n")


# def f13():
#    input=[chr(i) for i in range(91) if i>64]

#    print("F13:")
#    for n in input:
#        print ("\'"+n+"\'", end=" ")
#    print()


def f14():
    input = [' apple ', ' banana ', ' kiwi']
    output = [n.replace(" ", "", 2) for n in input]

    print("F14:")

    for n in input:
        print("\'" + n + "\'", end=" ")
    print()

    for n in output:
        print("\'" + n + "\'", end=" ")
    print("\n")


def main():
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    f9()
    f10()
    f11()
    f12()
    # f13()
    f14()


if __name__ == '__main__':
    main()
