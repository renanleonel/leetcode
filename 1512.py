nums = [1,2,3,1,1,3]

def numberOfGoodPairs(nums):
    goodPairs = 0
    hashmap = {}

    for i, num in enumerate(nums):
        if num in hashmap:
            goodPairs = goodPairs + hashmap.get(nums[i], 0)
        
        hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
    return goodPairs

print(numberOfGoodPairs(nums))