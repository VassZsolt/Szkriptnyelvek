#This program return the length of our string


def string_length(s):
    print("Your string is "+str(len(s))+" character length.")


if __name__ == '__main__':
    s = input('Give me a string: ')
    string_length(s)