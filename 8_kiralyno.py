def queen(representation):
    if len(representation) == 8:
        print("+-----------------+")
        temp = 7
        for i in range(8):
            print("|", end=" ")
            for j in range(8):
                if representation[j] == temp:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print("|")
            temp -= 1
        print("+-----------------+")


def main():
    representation = [7, 3, 0, 2, 5, 1, 6, 4]
    representation = [0, 4, 7, 5, 2, 6, 1, 3]
    queen(representation)


if __name__ == '__main__':
    main()
