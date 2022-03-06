from Szamjegyek_osszege import my_function

def test_myfunction():
    assert my_function(2,10)==7
    assert my_function(2,9)==8
    assert my_function(2,8)==13
    assert my_function(2,7)==11
    assert my_function(2,6)==10
    assert my_function(2,5)==5
    assert my_function(2,4)==7
    assert my_function(2,3)==8
    assert my_function(2,2)==4
    assert my_function(2,1)==2
    assert my_function(2,0)==1

