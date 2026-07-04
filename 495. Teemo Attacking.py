class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        tracker = 0
        sum1 = 0
        for x in timeSeries:
            if x>tracker:
                sum1 += x-tracker
            tracker = x + duration
        return timeSeries[-1]+duration-sum1


        