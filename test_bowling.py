from Bowling import scoreSheet



def test_strike_int_int():
    assert scoreSheet('X3/X922/X/234728').strike() == 250
    assert scoreSheet('21X5/39X/21X/2/X').strike() == 222
