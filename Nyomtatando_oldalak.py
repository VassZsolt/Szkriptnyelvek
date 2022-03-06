from typing import List


def nyomtatando_oldalak(bemenet: str) -> List[int]:
    datas = bemenet.split(',')
    interval = '-'
    oldalak = []
    for data in datas:
        if interval in data:
            interval_location = -1
            prefix = ""
            postfix = ""
            for index in range(len(data) - 1):
                if data[index] == interval:
                    interval_location = index
                if interval_location != -1:
                    postfix = postfix + data[index + 1]
            for i in range(interval_location):
                prefix = prefix + data[i]

            while int(prefix) < int(postfix) + 1:
                oldalak.append(int(prefix))
                prefix = str(int(prefix) + 1)

        else:
            oldalak.append(int(data))

    return oldalak


def main() -> None:
    # bemenet: str = input("Kérem agyja meg a nyomtatandó oldalakat:")
    bemenet: str = "1-4,7,9,11-15"
    print(nyomtatando_oldalak(bemenet))


if __name__ == '__main__':
    main()
