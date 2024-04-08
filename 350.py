nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersectionOfTwoArraysII(nums1, nums2):
    hashmap = {}
    res = []

    for num in nums1:
        hashmap[num] = 1 + hashmap.get(num, 0)
    
    for num in nums2:
        if num in hashmap and hashmap[num] > 0:
            hashmap[num] -= 1
            res.append(num)

    return res

print(intersectionOfTwoArraysII(nums1, nums2))