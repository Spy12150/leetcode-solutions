class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # There is no shot I solve this without AI help
        # Just the first idea to compare pl and sr and pr with sl i wouldve never thought of
        # and then after that i cba with all the syntaxing
        # surely no company quizzes me on this
        t = len(nums1)+len(nums2)-2
        if len(nums1) < len(nums2):
            p = nums1
            s = nums2
        else:
            p = nums2
            s = nums1

        start = 0
        end = len(p) 
        total = len(nums1) + len(nums2) 

        while start<=end:
            i = (start+end)//2
            j = total//2-i

            pl = p[i - 1] if i > 0 else float("-inf")
            pr = p[i] if i < len(p) else float("inf")
            sl = s[j - 1] if j > 0 else float("-inf")
            sr = s[j] if j < len(s) else float("inf")

            if pl>sr:
                end = i-1
            elif sl>pr:
                start = i+1
            else:
                left_max = max(pl, sl)
                right_min = min(pr, sr)
                if total %2 == 1:
                    return right_min
                return (left_max+right_min)/2
        left_max = max(pl, sl)
        right_min = min(pr, sr)
        if total %2 == 1:
            return right_min
        return (left_max+right_min)/2
        
