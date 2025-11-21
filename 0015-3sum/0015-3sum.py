class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for index, left in enumerate(nums):
            if index > 0 and left == nums[index-1]:
                continue

            middle, right = index+1, len(nums)-1

            while middle < right:
                total = left + nums[middle] + nums[right]
                if total < 0:
                    middle+=1
                elif total > 0:
                    right-=1
                else:
                    ans.append([left, nums[middle], nums[right]])
                    middle+=1
                    while nums[middle] == nums[middle-1] and middle < right:
                        middle+=1
        return ans