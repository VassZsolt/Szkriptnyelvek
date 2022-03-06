def clear_string(s):
    s = s.strip()
    cleaned_string = ""
    for index in range(len(s)):
        if s[index] != '\n' and s[index] != ' ':
            cleaned_string += s[index]

    return cleaned_string


def main():
    Test_string = "192.20.246.134:\n 6666"
    Test_string="206.130.99.82:\n8080"
    Test_string = "206. 130.99.82:\n8080"
    print(clear_string(Test_string))


if __name__ == '__main__':
    main()
