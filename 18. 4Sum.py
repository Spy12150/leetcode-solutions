class Solution(object):
    def fourSum(self, nums, target):
        answer = []
        answer2 = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    for a in range(z+1, len(nums)):
                        if  nums[x]+nums[y]+nums[z]+nums[a] == target:
                            answer.append(sorted([nums[x],nums[y],nums[z],nums[a]]))
        for h in answer:
            if h not in answer2:
                answer2.append(h)
        return answer2

Answer = Solution()
print(Answer.fourSum([1,0,-1,0,-2,2],0))