nums = [1, 2, 3, 4]

def paes(nums):
    ans = [1 for i in range(len(nums))]

    prefix, postfix = 1, 1
    
    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]

    for j in range(len(nums) -1, -1, -1):
        ans[j] *= postfix
        postfix *= nums[j]

        
    return ans

print(paes(nums))