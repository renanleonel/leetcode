nums = [2,15,11,7] 
target = 9

hashmap = {}

def twoSum(nums, target):
    for i, num in enumerate(nums):
        diff = target - num

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[num] = i


print(twoSum(nums, target))