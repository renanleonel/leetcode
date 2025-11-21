class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        ans = []
        visited = {}
        for i, n in enumerate(sortedNums):
            l, r = i + 1, len(sortedNums) - 1
            while l < r:
                if sortedNums[i] + sortedNums[l] + sortedNums[r] == 0:
                    possibleTriplet = [sortedNums[i], sortedNums[l], sortedNums[r]]
                    if tuple(possibleTriplet) not in visited:
                        ans.append(possibleTriplet)
                        visited[tuple(possibleTriplet)] = True
                    l += 1
                    r -= 1
                elif sortedNums[i] + sortedNums[l] + sortedNums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return ans