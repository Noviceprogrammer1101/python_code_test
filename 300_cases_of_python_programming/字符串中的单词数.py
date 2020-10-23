class  Solution:

    def countSegement(self,s):
        res=0
        for i in range(len(s)):
            if s[i]!=' ' and(i==0 or s[i-1]==' '):
                res+=1
        return res


s=Solution()
n='Hello, my name is Join'
print('input: ',n)
print('output',s.countSegement(n))