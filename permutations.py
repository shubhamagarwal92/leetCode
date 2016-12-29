## Based on DFS
class Solution(object):
    def permute(self, nums):
        size=len(nums)
        temp=[]
        result=[]
        result=self.myFunc(result,nums,temp,size)
        return result
    
    def myFunc(self,result,nums,temp,size):
        if len(temp)==size:
            result.append(temp[:])
            return result
        for i in range(0,len(nums)):
            temp1=nums[:]
            temp.append(nums[i])
            del temp1[i]
            result=self.myFunc(result,temp1,temp,size)
            temp.pop()
        return result


nums = [1,2,3]
permutations = Solution()
solution = permutations.permute(nums)
print "Total number of solution: " + str(len(solution))
print solution
