#bruteForce Approch
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if((nums[i]+nums[j])==target):
                    return(i,j)
        
        
        
   #another solution
   class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(len(nums)):
            if target-nums[i] in ans:
                return([ans[target-nums[i]],i])
                
            else:
                ans[nums[i]]=i
