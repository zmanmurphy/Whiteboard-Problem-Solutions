from groupAnagrams import groupAnagrams

def test_group_anagrams():
    # Test case 1: Basic test with multiple anagrams
    input_strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    expected_output = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
    result = groupAnagrams(input_strs)
    assert result == expected_output

    # Test case 2: Single string input
    input_strs = ["x"]
    expected_output = [["x"]]
    result = groupAnagrams(input_strs)
    assert result == expected_output

    # Test case 3: Empty input list
    input_strs = []
    expected_output = []
    result = groupAnagrams(input_strs)
    assert result == expected_output

    # Test case 4: No anagrams present
    input_strs = ["abc", "def", "ghi"]
    expected_output = [["abc"], ["def"], ["ghi"]]
    result = groupAnagrams(input_strs)
    assert result == expected_output