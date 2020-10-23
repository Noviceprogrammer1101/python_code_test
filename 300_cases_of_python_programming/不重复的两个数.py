class Solution:
    def theTwoNumbers(self,a):
        ans=[0,0]
        for i in a:
            ans[0]=ans[0]^i
        c=1
        while c & ans[0]!=c:
            c=c<<1
        for i in a:
            if i &c==c:
                ans[1]=ans[1]^i
        ans[0]=ans[0]^ans[1]
        return ans

arr=[1,2,5,1]
solution=Solution()
print('数组： ',arr)
print('两个没有重复的数字： ',solution.theTwoNumbers(arr))
