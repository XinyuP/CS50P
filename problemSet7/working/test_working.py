from working import convert
import pytest

def test_AM():
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"
    assert convert("1:00 AM to 11:00 AM") == "01:00 to 11:00"

def test_AM_minute():
    assert convert("1:23 AM to 11:43 AM") == "01:23 to 11:43"


def test_PM():
    assert convert("1 PM to 10 PM") == "13:00 to 22:00"
    assert convert("2:00 PM to 7:00 PM") == "14:00 to 19:00"

def test_PM_minute():
    assert convert("4:07 PM to 9:50 PM") == "16:07 to 21:50"


def test_12():
    assert convert("12 PM to 12 PM") == "12:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 AM") == "00:00 to 00:00"

    assert convert("12:02 PM to 12:49 PM") == "12:02 to 12:49"
    assert convert("12:01 AM to 12:59 PM") == "00:01 to 12:59"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"



def test_exceed_limit():
    with pytest.raises(ValueError):
        convert("1:60 AM to 11:00 AM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 11:00 AM")
    with pytest.raises(ValueError):
        convert("-1:60 AM to 11:00 AM")
    with pytest.raises(ValueError):
        convert("1:60 PM to 11:-3 PM")




def test_invalid_format():
    with pytest.raises(ValueError):
        convert("1:60 AM - 11:00 AM")
    with pytest.raises(ValueError):
        convert("13:00AM to 11:00 AM")
    with pytest.raises(ValueError):
        convert("-1:60 AM to 11:00PM")
    with pytest.raises(ValueError):
        convert("cat")

































