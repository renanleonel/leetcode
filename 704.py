nums = [-1,0,3,5,9,12]
target = 9

def binarySearch(nums, target):
    l, r = 0, len(nums) -1
    while l <= r:
        m = (l + r) // 2

        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m

    return -1

   
print(binarySearch(nums, target))

