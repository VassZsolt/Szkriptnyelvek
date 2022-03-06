def my_function(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    if len(word1) == len(word2):
        for letter in word1:
            for letter2 in word2:
                if letter == letter2:
                    word2 = word2.replace(letter2, "")
    result = False
    if len(word2) == 0:
        result = True
        return result
    else:
        return result


def my_function2(word1, word2): #This is the trivial solution
    word1 = sorted(word1.lower().replace(" ", ""))
    word2 = sorted(word2.lower().replace(" ", ""))

    result = False
    if word1 == word2:
        result = True
        return result
    else:
        return result


def main():
    word1 = "A gentleman"
    word2 = "Elegant man"
    answer = my_function2(word1, word2)
    print("Anagramma? ", answer)


if __name__ == '__main__':
    main()
