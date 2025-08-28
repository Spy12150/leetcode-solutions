import math
class Solution(object):
    def distance(self, l1, l2):
        return math.sqrt((abs(l2[1] - l1[1]))**2+(abs(l2[0] - l1[0]))**2)
    def validSquare(self, p1, p2, p3, p4):
        a = self.distance(p1,p2)
        b = self.distance(p1,p3)
        c = self.distance(p1,p4)
        d = self.distance(p2,p3)
        e = self.distance(p2,p4)
        f = self.distance(p3,p4)
        if a == 0 or b ==0 or c ==0 or d==0 or e==0 or f==0:
            return False
        score1 = [a]
        score2 = []
        if a == b:
            score1.append( b)
        else:
            score2.append( b)
        if a == c:
            score1.append( c)
        else:
            score2.append( c)
        if a == d:
            score1.append( d)
        else:
            score2.append( d)
        if a == e:
            score1.append( e)
        else:
            score2.append( e)
        if a == f:
            score1.append( f)
        else:
            score2.append( f)
        if len(score1) == 4 and len(score2) == 2:
            for x in range(0,len(score1)):
                if score1[x] != score1[x-1]:
                    return False
            for x in range(0,len(score2)):
                if score2[x] != score2[x-1]:
                    return False    
            return True
        if len(score1) == 2 and len(score2) == 4:
            for x in range(0,len(score1)):
                if score1[x] != score1[x-1]:
                    return False
            for x in range(0,len(score2)):
                if score2[x] != score2[x-1]:
                    return False   
            return True
        return False
        

Answer = Solution()
print(Answer.validSquare([0,0],[1,1],[1,0],[0,1]))
        