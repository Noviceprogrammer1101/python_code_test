class Solution:

    def isTwin(self,s,t):
        if len(s)!=len(t):
            return "NO"

        adds=[]
        evens=[]

        addt=[]
        event=[]
        for i in len(s):
            if i & 1:
                adds.append(s[i])
                addt.append(t[i])
            else:
                evens.append(s[i])
                event.append(t[i])

        adds.sort()
        addt.sort()
        evens.sort()
        event.sort()

        for i in adds:
            if i in addt:
                return "true"
            else:
                return "NO"


s="abcd"
t="cadb"
s=Solution()
print("s and t ",s,t)
print("是否为双胞胎： ",s.isTwin(s,t))
