class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lst=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                lst.append(nums[i])
        for i in lst:
            nums.remove(i)
        return len(nums)
solution = Solution()
nums = [0,0,1,1, 1, 2,2,3,3,4]
result = solution.removeDuplicates(nums)
print(result)  # Output: 2
print(nums)