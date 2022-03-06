class Sor:
    def __init__(self):
        self.data = []

    def betesz(self, value):
        self.data.append(value)
        return self.data

    def kivesz(self):
        if self.ures():
            return None
        else:
            return self.data.pop(0)


    def meret(self):
        return len(self.data)

    def ures(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        data2=[]
        i=len(self.data)-1
        while i > -1:
            data2.append(self.data[i])
            i-=1
        return str(data2)


def main():

    s = Sor()
    print(s)
    print(s.ures())
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)
    print(s.meret())
    print(s.ures())
    x = s.kivesz()
    print(x)
    print(s)
    s.kivesz()
    s.kivesz()
    x = s.kivesz()
    print(x)

    
if __name__ == '__main__':
    main()
