def Intermediate_string():
    s ="I"
    s2 = '{:>3}'.format(s)
    print(s2)
    s="Can"
    s2 = '{:>6}'.format(s)
    print(s2)
    s="Manipulate"
    s2 = '{:>14}'.format(s)
    print(s2)
    s="String"
    s2 = '{:>11}'.format(s)
    print(s2)
    s="Alignment"
    s2 = '{:>15}'.format(s)
    print(s2)


def main():
    Intermediate_string()


if __name__ == '__main__':
    main()