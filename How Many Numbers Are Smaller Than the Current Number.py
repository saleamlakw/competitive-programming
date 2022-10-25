class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ch=[]
        for i in nums:
            a=0
            for k in nums:
                if i>k:
                    a+=1
            ch.append(a)
        return(ch)
