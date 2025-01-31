''' My Test Calculator '''

def test_basic_math():
    '''Test that addition works'''
    assert 1+1 == 2

def test_another_math():
    '''Test that addition works'''
    result = 2 * 5
    expected = 10
    assert result == expected, f"Expected{expected}, got {result}"
