from Anagramma import my_function


def test_my_function():
    assert my_function("listen", "silent") == True
    assert my_function("listen", "silentt") == False
    assert my_function("A gentleman", "Elegant man") == True
    assert my_function("A gentleman", "Elegant mans") == False
    assert my_function("Clint Eastwood", "Old west action") == True
    assert my_function("Clint Eastwood", "Old west actions") == False
    assert my_function("dormitory", "dirty room") == True
    assert my_function("dormitories", "dirty room") == False
