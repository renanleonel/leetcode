nums = [1,2,3,1]
k = 3

def containsDuplicateII(nums, k):
    hashmap = {}

    for i in range(len(nums)):
        if nums[i] in hashmap:
            if abs(hashmap[nums[i]] - i) <= k:
                return True

        hashmap[nums[i]] = i
    
    return False



print(containsDuplicateII(nums, k))