class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans=0
        while sorted(nums) != nums:
            ans+=1
            s = 0
            m = float("inf")
            n = 0
            for i in range(1, len(nums)):
                s = nums[i] + nums[i-1]
                if s < m:
                    m = s
                    n = i
            nums = nums[:n-1] + [m] + nums[n+1:]
        return ans