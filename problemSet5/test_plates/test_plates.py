from plates import is_valid

def test_start_with_Two():
    assert is_valid("C1") == False
    assert is_valid("CS50") == True
    assert is_valid("CS5000") == True
    assert is_valid("50CS") == False
    assert is_valid("50789") == False
    assert is_valid("BlAIRE") == True

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("CSCS50") == True
    assert is_valid("CSCS500") == False
    assert is_valid("CSPython") == False
    assert is_valid("CSPython110") == False

def test_number_middle():
    assert is_valid("CS50X") == False
    assert is_valid("CSS500") == True
    assert is_valid("CS1X") == False
    assert is_valid("CSE098") == False

def test_periods_spaces_punctuation():
    assert is_valid("CS50.") == False
    assert is_valid("CS50,") == False
    assert is_valid("CS50 ") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50 ") == False
    assert is_valid("CS!@!") == False
    





