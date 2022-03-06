INPUT = """\"A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.\""""


def text_change(INPUT):
    d = {}
    d['Á'] = 'A'
    d['É'] = 'E'
    d['Í'] = 'I'
    d['Ó'] = 'O'
    d['Ö'] = 'O'
    d['Ő'] = 'O'
    d['Ú'] = 'U'
    d['Ü'] = 'U'
    d['Ű'] = 'U'
    # The dictonary contains the characters which should be changed

    OUTPUT = ""
    temp = ""
    for character in INPUT:
        if character in d.keys():  # if the char is uppercase and should be changed
            OUTPUT += d[character]
        elif character.upper() in d.keys():  # if the char is lowercase and should be changed
            temp = d[character.upper()]
            OUTPUT += temp.lower()
        else:
            OUTPUT += character
    return OUTPUT


def main():
    answer=text_change(INPUT)
    print(answer)

if __name__ == '__main__':
    main()
