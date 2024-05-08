nums = [1,2,5,2,3]
target = 5

def targetIndices(nums, target):
    ans = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] == target:
            ans.append(i)

    return ans


print(targetIndices(nums, target))

