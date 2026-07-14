class Solution:

    # for slightly faster results, calculate h in the helper function and compare it outside
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        def caneat(rate):
            #print(1)
            hours = 0
            for pile in piles:
                hours += (pile+rate-1)//rate
            if hours <= h:
                return True
            else: 
                return False

        while start < end:
            mid = (end+start) // 2
            #print(start,mid,end)
            #print(caneat(start), caneat(mid), caneat(end), h, piles)
            #print(start,end,mid)
            #if caneat(mid) <= h and caneat(mid-1) > h:
                #return mid
            if caneat(mid):
                end = mid
            else:
                start=mid+1
        return start
