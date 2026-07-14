class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start<end:
            start1 = nums[start]
            end1 = nums[end]
            mid = (start+end)//2
            mid1 = nums[mid]
            #print(start1, mid1, end1)
            if start1 == end1:
                if start1 == mid1:
                    start= start+1
                elif start1 > mid1:
                    end = mid
                elif start1 < mid1:
                    start = mid
            elif start1 == mid1 and mid1 < end1:
                return mid1
            elif start1 <= mid1 and mid1 > end1:
                start = mid+1
            elif start1 < mid1 and mid1<= end1:
                return start1
            elif start1 > mid1 and mid1<= end1:
                end = mid
        return nums[start]
    
    #there is simpler solution, you dont actually ahvfe to look at left at all.
        