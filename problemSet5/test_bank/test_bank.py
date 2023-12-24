from bank import value

def test_0():
    assert value("HELLO") == 0
    assert value("heLLO") == 0
    assert value("heLLO, blaire") == 0
    assert value("helLOoooOO") == 0
    assert value("HELLOOO") == 0
    assert value("HELLOOO!!!?") == 0
    

def test_20():
    assert value("hehe") == 20
    assert value("Hehe") == 20
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hate you so much") == 20
    assert value("Hey Hello") == 20
    
    

def test_100():
    assert value("Goodmorning") == 100
    assert value("1234") == 100
    assert value("What's up") == 100
    assert value("!What's up") == 100
    assert value(".,!@#What's up") == 100
    assert value("lmao hello") == 100

   





