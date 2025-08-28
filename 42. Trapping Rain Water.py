class Solution(object):
    def trap(self, height):
        lrlist = []
        rllist = []
        sollist = []
        value = 0
        for x in height:
            if x>value:
                value = x
                lrlist += [0]
            else:
                lrlist += [value-x]
        height.reverse()
        value = 0
        for x in height:
            if x>value:
                value = x
                rllist += [0]
            else:
                rllist += [value-x]
        rllist.reverse()
        for a in range(0,len(lrlist)):
            sollist+=[min(lrlist[a],rllist[a])]
        return sum(sollist)

Answer = Solution()
print(Answer.trap([0,1,0,2,1,0,1,3,2,1,2,1]))