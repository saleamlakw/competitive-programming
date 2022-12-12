class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            try:
                f=0
                for h in nums2[(nums2.index(i))+1:]:
                    if h>i:
                        ans.append(h)
                        f+=h
                        break
                if i>f:
                    ans.append(-1)
            except:
                ans.append(-1)
        return ans
