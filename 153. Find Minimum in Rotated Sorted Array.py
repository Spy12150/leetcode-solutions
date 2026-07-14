class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = (start+end+1)//2
            print(start, mid, end)
            if nums[end] >= nums[start]:
                return nums[start]
            elif nums[mid] > nums[end]:
                start = mid+1
            elif nums[mid] < nums[end]:
                end = mid 
        