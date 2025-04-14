from Leetcode.三数之和 import solution


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 从后向前找到第一个升序对 (i, i+1)，即 nums[i] < nums[i+1]
        # 2. 如果没有找到，说明当前排列是最大的，直接反转整个数组
        # 3. 如果找到了，继续从后向前找到第一个比 nums[i] 大的元素 j
        # 4. 交换 nums[i] 和 nums[j]
        # 5. 反转 nums[i+1:] 部分
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])
# Example usage:
solution=Solution()
nums = [1, 2, 3]
solution.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]