nums = [4,5,4]

def majorityElement(nums):
    hashmap = {}
    n = len(nums)

    for num in nums:
        hashmap[num] = 1 + hashmap.get(num, 0)

    for num in hashmap:
        if hashmap[num] > n/2:
            return num

print(majorityElement(nums))