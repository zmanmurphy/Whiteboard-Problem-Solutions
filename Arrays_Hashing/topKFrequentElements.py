def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
        
    array = []
    for num, cnt in count.items():
        array.append([cnt, num])
    array.sort()

    results = []
    while len(results) < k:
        results.append(array.pop()[1])
    return results

def main():
    nums = [1,2,2,3,3,3]
    k = 2
    print(topKFrequent(nums, k))
    nums = [7,7]
    k = 1
    print(topKFrequent(nums, k))

if __name__ == "__main__":
    main()