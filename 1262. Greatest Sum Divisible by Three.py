class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        listof1 = []
        listof2 = []
        for x in nums:
            if x%3 == 1:
                listof1 += [x]
            if x%3 == 2:
                listof2 += [x]
        listof1.sort()
        listof2.sort()
        if total % 3 == 1:
            if len(listof2) < 2:
                return total-listof1[0]
            return max(total - listof1[0], total-sum(listof2[:2]))
        if total %3 == 2:

            if len(listof1) < 2:
                return total-listof2[0]
            if len(listof2) < 1:
                return total-sum(listof1[0:2])
            return max(total-sum(listof1[:2]),total - listof2[0])
        else:
            return total
        
