from fuel import convert, gauge
import pytest

def test_convert_happy():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("2/5") == 40
    assert convert("1/7") == 14
    assert convert("3/8") == 38


def test_convert_ValueError_str():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1/dog") 
    with pytest.raises(ValueError):
        convert("cat/2") 


def test_convert_ValueError_float():
    with pytest.raises(ValueError):
        convert("1.2/3")


def test_convert_ValueError_x_greater_y():
    with pytest.raises(ValueError):
        convert("3/2")


def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0") 
    with pytest.raises(ZeroDivisionError):
        convert("0/0") 
    

def test_convert_0_100():
    assert convert("0/1") == 0
    assert convert("10/10") == 100

def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percent():
    assert gauge(23) == "23%"








