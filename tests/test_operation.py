from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(5,3)==8
    assert add(7,5)==12

def test_sub():
    assert sub(5,3)==2
    assert sub(4,1)==3
    assert sub(2,2)==0
    assert sub(7,6)==1
