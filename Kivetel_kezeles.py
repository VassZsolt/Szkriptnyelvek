def my_func():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))

            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ValueError as e1:
            print("Kérem csak számokat adjon meg!")
        except KeyboardInterrupt as e2:
            return
        except ZeroDivisionError as e3:
            print("Nullával nem lehet osztani (tehát a második szám nem lehet 0).")

def main():
    my_func()

#####

if __name__ == "__main__":
    main()