class Solution:


    def binarySearch(self,nums,target):
        return self.search(nums,0,len(nums)-1,target)

    def search(self,nums,start,end,target):
        if start>end :
            return -1
        mid=(start+end)//2

        if nums[mid]==target:
            return mid

        if nums[mid]>target:
            return self.search(nums,start,mid,target)
        if nums[mid]<target:
            return self.search(nums,mid,end,target)

if __name__=='__main__':
    my_solution=Solution()
    nums=[1,4,3,2,5,8]
    target=3
    targetindex=my_solution.binarySearch(nums,target)
    print('input: nums= ',nums," ","target= ",target)
    print("output: ",targetindex)