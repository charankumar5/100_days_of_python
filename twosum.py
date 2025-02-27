class Solution:
    nums = [3,4,9,6,4]
    target = 8
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return [i,j]
    
test_solution = Solution()

print(test_solution.twoSum(nums = [3,4,9,6,4],target = 8))