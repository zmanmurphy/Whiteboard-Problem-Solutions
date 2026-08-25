def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer: list[int] = [i, j]
                    return answer

def main():
    nums = [4, 5 , 6]
    target = 10
    print(twoSum(nums, target))
    nums = [3, 4, 5, 6]
    target = 7
    print(twoSum(nums, target))

if __name__ == "__main__":
    main()