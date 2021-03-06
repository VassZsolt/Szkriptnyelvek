from Median import median


def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([3, 1, 2, 5, 3]) == 3
    assert median([1, 300, 2, 200, 1]) == 2
    assert median([3, 6, 20, 99, 10, 15]) == 12.5

