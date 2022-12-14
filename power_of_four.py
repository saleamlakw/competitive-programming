class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            a=math.log(n,4)
            if abs(round(a)-a)<0.1 and 4*round(a)==n:
                b=round(a)
            else:
                b=a
            if b==int(b):
                return True
            else:
                return False
