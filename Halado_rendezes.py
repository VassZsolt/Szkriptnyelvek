data = [
    (1, 'Albany', 'NY', 162692),
    (3, 'Allegany', 'NY', 11986),
    (121, 'Wyoming', 'NY', 8722),
    (123, 'Yates', 'NY', 5094)
]
users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

li=[ [2,6],[1,3],[5,4]]


def my_func1(t):
    return t[-1]


def my_func2(user):
    return int(user.split(':')[0])

def my_func3(li):
    return str(li[1])


def main():
    result1_1 = sorted(data, key=my_func1)
    print(result1_1)

    result1_2 = sorted(data, key=lambda t: t[-1])
    print(result1_2)

    result2_1 = sorted(users, key=my_func2, reverse=True)
    print(result2_1)

    result2_2 = sorted(users, key=lambda user:int(user.split(':')[0]), reverse=True)
    print(result2_2)

    result3_1 = sorted(li, key=my_func3)
    print(result3_1)

    result3_2 = sorted(li, key=lambda li:str(li[1]))
    print(result3_2)

if __name__ == '__main__':
    main()
