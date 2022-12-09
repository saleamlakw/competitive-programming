class Solution:
    def isValid(self, s: str) -> bool:
            open=[]
            all=[]
            inde=[]
            alldic={"{":"}","(":")","[":"]"}
            result=False
            for i in range(len(s)):
                all.append(s[i])
                if s[i]=="(" or s[i]=="{" or s[i]=="[":
                    open.append(s[i])
                    inde.append(i)
            for i in range(len(open)):
                if len(s)%2!=0 or len(open)!=len(all)/2: 
                    result=False
                    break
                else:
                    try:
                            if alldic[open[-1]]==all[inde[-1]+1]:
                                result=True
                                all.pop(inde[-1]+1)
                                all.pop(inde[-1])
                                open.pop()
                                inde.pop()
                            else:
                                result=False
                                break
                    except:
                            result=False
                            break
            return result
