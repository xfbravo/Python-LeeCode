class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        maxArea=0
        while left<right:
            maxArea=max(maxArea, min(height[left], height[right])*(right-left))
            preLeft=left#记录上一个left的值
            preRight=right#记录上一个right的值
            if height[left]<height[right]:#如果左边的高度小于右边的高度
                left+=1#向右移动left
                while height[left]<=height[preLeft]and left<right:#如果新的left的高度小于等于上一个left的高度，那么Area一定小于maxArea（因为宽度在降低），继续向右移动
                    left+=1
            else:                                                #这样就不用每次移动都要计算Area，大大降低了时间复杂度
                right-=1
                while height[right]<height[preRight] and left<right:#如果新的right的高度小于等于上一个right的高度，那么Area一定小于maxArea，继续向左移动
                    right-=1
        return maxArea
solution=Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # 49