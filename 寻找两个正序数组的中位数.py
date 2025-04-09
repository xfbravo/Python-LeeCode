class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        #和平分合并两个有序数组，并重新排序
        nums=sorted(nums1 + nums2)
        #记录合并后数组的长度
        n=len(nums)
        #如果长度为奇数，返回中位数
        if n%2==1:
            return round(float(nums[n//2]),5)
        #如果长度为偶数，返回中位数
        else:
            return round(float((nums[n//2-1]+nums[n//2])/2),5)
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2])) # 2.0