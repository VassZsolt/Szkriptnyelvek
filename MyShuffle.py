import random
from typing import List


def shuffled(li: List[int]) -> List[int]:
    copy=li[:] #li.copy
    random.shuffle(copy)
    return copy


def main():
    li = [3, 8, 2, 8, 4, 2, 1, 9]
    print(li)
    print(shuffled(li))
    print(shuffled(li)[-1])


if __name__ == '__main__':
    main()
