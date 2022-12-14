class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
                return False
        else:
                b=math.log(n,3)
                if abs(round(b)-b)<0.1 and (3**round(b)==n):
                        a=round(b)
                else:
                        a=b
                if a==int(a):
                        return True
                else:
                        return False
            
        
