nums = [0,1,4,6,7,10]
diff = 3

def arithmeticTriplets(nums, diff):
    hashmap = {}
    ans = 0

    for i in range(len(nums)):
        if nums[i] - diff in hashmap and nums[i] - 2*diff in hashmap:
            ans +=1
        
        hashmap[nums[i]] = 1
    
    return ans

print(arithmeticTriplets(nums, diff))