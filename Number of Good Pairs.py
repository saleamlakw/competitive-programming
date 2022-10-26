class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int: 
        all=0
        for i in range(len(nums)):
            a=nums[nums.index(nums[i])+1:]
            for k in range(len(a)):
                if nums[i]==a[k]:
                    all+=1
            nums[i]="d"
        return all
        
