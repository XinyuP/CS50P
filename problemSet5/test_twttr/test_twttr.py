from twttr import shorten

def test_shorten_number():
    assert shorten("1234") == "1234"
    assert shorten("A1234") == "1234"
    assert shorten("A12C34") == "12C34"
    
def test_shorten_symbol():
    assert shorten(",.<>") == ",.<>"
    assert shorten(",.a<>") == ",.<>"
    assert shorten(",.c<>e") == ",.c<>"


def test_shorten_mix():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert("CS50") == "CS50"































