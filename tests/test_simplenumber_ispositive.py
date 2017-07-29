from simplenumber import SimpleNumber

def test_positive():
    number = SimpleNumber(1)
    assert number.is_positive()

def test_negative():
    number = SimpleNumber(-1)
    assert not number.is_positive()

'''
Uncomment this test to ensure the mutation testing passes.
It tests the boundary condition of isPositive
'''
#def test_boundary():
#    number = SimpleNumber(0)
#    assert number.is_positive()
