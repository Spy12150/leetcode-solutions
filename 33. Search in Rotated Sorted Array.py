class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        while start < end:
            
            mid = (start+end)//2
            l = nums[start]
            m = nums[mid]
            r = nums[end]
            #print(start, mid, end)
            if m == target:
                return mid
            elif l<m:
                if target >= l and target<m:
                    end = mid
                else:
                    start = mid+1
            elif m<l:
                if target > m and target <= r:
                    start = mid+1
                else:
                    end = mid
            else:
                start = mid+1
        #print(start, end)
        if nums[start] == target:
            return start
        return -1
