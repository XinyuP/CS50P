from numb3rs import validate

def test_one_digit():
    assert validate("0.0.0.0") == True
    assert validate("0.1.2.3") == True
    assert validate("9.0.0.0") == True
    assert validate("9.9.0.9") == True

def test_two_digits():
    assert validate("29.10.20.30") == True
    assert validate("99.1.1.1") == True
    assert validate("99.1.1.1") == True

def test_three_digits():
    assert validate("251.10.200.30") == True
    assert validate("99.111.1.3") == True
    assert validate("99.87.249.1") == True


# def test_leading_0():
#     assert validate("0.01.0.0") == False
#     assert validate("0.023.0.0") == False
#     assert validate("10.01.10.10") == False


def test_over_255():
    assert validate("255.255.255.256") == False
    assert validate("499.893.324.2333") == False
    assert validate("1.0.0.3000") == False
    assert validate("290.0.0.0") == False


def test_invalid_input():
    assert validate("cat") == False
    assert validate("moew.moew.moew.moew") == False
    assert validate("102.0.1.moew") == False
    assert validate("moew.102.moew.102") == False
    assert validate("102.moew.102.moew") == False
    assert validate("102.moew.102.moew.") == False
    assert validate("255.255.255.255.") == False
    assert validate(".255.255.255.255") == False

def test_shorter_input():
    assert validate("0.1.2") == False
    assert validate("0.3") == False
    assert validate("0") == False


def test_longer_input():
    assert validate("0.1.2.3.4") == False
    assert validate("0.1.2.3.999") == False
