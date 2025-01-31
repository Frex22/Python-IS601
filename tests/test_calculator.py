def test_basic_math():
    assert 1+1 == 2

def test_another_math():
    result = 2 * 5
    expected = 10
    assert result == expected, f"Expected{expected}, got {result}"