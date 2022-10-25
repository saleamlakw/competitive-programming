class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        li=[]
        if nums.count(target)>1:
            for i in range(nums.count(target)):
               li.append(nums.index(target))
               nums[nums.index(target)]=1000
        else:
           try:
            li.append(nums.index(target))
           except:
            li=[]
        return(li)

