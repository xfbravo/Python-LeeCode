class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
solution = Solution()
nums = [3,2,2,3]
val = 3
result = solution.removeElement(nums, val)
print(result)  # Output: 2
print(nums)  # Output: [2, 2]