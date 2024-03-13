nums = [1,1,1,2,2,3]
k = 2

def topK(nums, k):
    hashmap = {}
    ans = []
    
    for i, num in enumerate(nums):
        hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
    
    i = 0

    sortedMap = sorted(hashmap, key=hashmap.get, reverse=True)

    while i < k:
        ans.insert(i, sortedMap.pop(0))
        i+=1

    return ans

print(topK(nums, k))