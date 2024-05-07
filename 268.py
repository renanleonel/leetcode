nums = [9,6,4,2,3,5,7,0,1]

def missingNumber(nums):
    hashmap = {}

    for num in nums:
        hashmap[num] = 1

    for i in range(len(nums)):
        if i not in hashmap:
            return i

    return len(nums)

print(missingNumber(nums))

