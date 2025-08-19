class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                cnt+=1
            else:
                res+=(cnt*(cnt+1))//2
                cnt=0
        res+=(cnt*(cnt+1))//2
        return res