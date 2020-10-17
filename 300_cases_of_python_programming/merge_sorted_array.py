class Solution:
    def mergerSortedArray(self,A,B):
        i,j=0,0
        c=[]
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                c.append(A[i])
                i+=1
            else:
                c.append(B[j])
                j+=1
        while i<len(A):
            c.append(A[i])
            i+=1
        while j<len(B):
            c.append(B[i])
            j+=1
        return c

# 主函数
if __name__=='__main__':

    A=[1,2,3]
    B=[1,4]
    # A=input('input A array: ')
    # B=input('input B array: ')
    solution=Solution()
    print("output: ",solution.mergerSortedArray(A,B))
