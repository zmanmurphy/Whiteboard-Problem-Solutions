
def hasDuplicate(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
    
def main():
    nums = [1,2,3,3]
    print(hasDuplicate(nums))
    nums = [1,2,3,4]
    print(hasDuplicate(nums))

if __name__ == "__main__":
    main()