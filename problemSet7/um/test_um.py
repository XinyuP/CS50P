from um import count


def test_solo():
    assert count("um") == 1
    assert count("Um") == 1
    assert count(" Um ") == 1
    assert count("uM ") == 1
    assert count(" uM") == 1


def test_um_in_word():
    assert count("umm") == 0
    assert count("uum") == 0
    assert count("umum") == 0


def test_um_in_sentence():
    assert count("um..") == 1
    assert count(".um.") == 1

def test_um_multiple():
    assert count("um um") == 2
    assert count("um,um") == 2
