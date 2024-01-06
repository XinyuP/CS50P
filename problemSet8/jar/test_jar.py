from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert jar.size == 1
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert jar.size == 4
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(2)
    assert jar.size == 4
    jar.deposit(8)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(-1)
    
def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.withdraw(12)






