from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

def main():
    input_strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    result = groupAnagrams(input_strs)
    print(result)
    input_strs = ["x"]
    result = groupAnagrams(input_strs)
    print(result)

if __name__ == "__main__":
    main()