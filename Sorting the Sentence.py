class Solution:
    def sortSentence(self, s: str) -> str:
        y={}
        z=[]
        a=s.split()
        for k in a:
            y[int(k[-1])]="".join(k[:-1])
        for i in range(1,len(a)+1):
            z.append(y[i])
        return(" ".join(z))
