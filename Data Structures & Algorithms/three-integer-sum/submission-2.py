class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        set1 = set()
        returnlist = []
        for num in range(len(nums)):
            left = num+1
            right = len(nums)-1
            while(left<right):
                sum = nums[left]+ nums[right]+ nums[num]
                if(sum>0):
                    right-=1
                elif(sum<0):
                    left+=1
                elif(sum==0):
                    set1.add((nums[left],nums[right],nums[num]))
                    left+=1
        for tuples in set1:
            returnlist.append(list(tuples))
        return returnlist
        #return list1

                

