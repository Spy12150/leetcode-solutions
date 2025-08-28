class Solution(object):
    def removeDuplicates(self, nums):
        nums.append(0.1)
        removallist = []
        for x in range(0,len(nums)):
            if nums[x] == nums[x-1]:
                removallist += [nums[x]]
        for y in removallist:
            nums.remove(y)
        nums.remove(0.1)
        return len(nums)

Answer = Solution()
print(Answer.removeDuplicates([1,1,2]))