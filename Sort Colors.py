class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b=[]
        for k in range(max(nums)+1):
            for i in range(nums.count(k)):
                b.append(k)
        for j in range(len(nums)):
            nums[j]=b[j]
