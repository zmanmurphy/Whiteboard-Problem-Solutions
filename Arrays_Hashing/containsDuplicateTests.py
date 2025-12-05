from containsDuplicate import hasDuplicate

def test_containsDuplicate():
    nums = [1,4,4,5,7]
    assert hasDuplicate(nums) == True
    nums = [1,2,3,4,5,6,7]
    assert hasDuplicate(nums) == False
    nums = [1,2,2,3,3,4]
    assert hasDuplicate(nums) == True

