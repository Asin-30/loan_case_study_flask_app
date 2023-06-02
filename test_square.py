from square import square_fun

def test_square_fun():
    a = 4
    result = square_fun(a)

    # assert the observed (result) value with the expected value
    assert result == 16
