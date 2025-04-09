class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        minGap=10000000
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if abs(total-target)<abs(minGap-target):
                    minGap=total
                if total==target:
                    return total
                elif total<target:
                    while nums[left]==nums[left+1] and left<right-1:
                        left+=1
                    left+=1
                else:
                    while nums[right]==nums[right-1] and left<right-1:
                        right-=1
                    right-=1

        return minGap
solution=Solution()
print(solution.threeSumClosest([10,20,30,40,50,60,70,80,90], 1))