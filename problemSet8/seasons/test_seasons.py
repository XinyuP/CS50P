from seasons import Birthday
import pytest

def test_valid():
    assert Birthday("2023-01-06").get_minute() == "Five hundred twenty-five thousand, six hundred minutes"
    assert Birthday("2022-01-06").get_minute() == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_format():
    with pytest.raises(SystemExit):
        Birthday("2023-01-062")
    with pytest.raises(SystemExit):
        Birthday("cat")
    with pytest.raises(SystemExit):
        Birthday("January 1, 1999")
    
def test_logic_error():
    with pytest.raises(SystemExit):
        Birthday("2023-00-02").get_minute()