nums = [1,1,1,2,2,3]
k = 2

def topK(nums, k):
    ans = []
    hashmap = {}
    frequency = [[] for i in range(len(nums) + 1)]
    
    for num in nums:
        hashmap[num] = 1 + hashmap.get(num, 0)
    
    for num, occurency in hashmap.items():
        frequency[occurency].append(num)

    for j in range (len(nums), 0, -1):
        for num in frequency[j]:
            ans.append(num)

            if len(ans) == k:
                return ans

print(topK(nums, k))