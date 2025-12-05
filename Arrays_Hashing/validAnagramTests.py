from validAnagram import isAnagram

def test_isAnagram():
    assert isAnagram("are", "ear") == True
    assert isAnagram("hi", "no") == False
    assert isAnagram("flow", "wolf") == True
    assert isAnagram("doubt", "stab") == False