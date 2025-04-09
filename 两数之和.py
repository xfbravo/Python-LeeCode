class Solution:
    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
print(Solution().twoSum([3,2,4], 6))