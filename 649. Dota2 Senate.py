class Solution(object):
    def predictPartyVictory(self, senate):
        from collections import deque 
        rad = deque()
        dire = deque()
        n = len(senate)

        for idx, senator in enumerate(senate):
            if senator == "R":
                rad.append(idx)
            else:
                dire.append(idx)

        while rad and dire:
            rad_sen = rad.popleft()
            dire_sen = dire.popleft()

            if rad_sen < dire_sen:
                rad.append(rad_sen+n)
            else:
                dire.append(rad_sen+n)

        if rad:
            return "Radiant"
        return "Dire"


        
#Old bad solution
"""
class Solution(object):
    def predictPartyVictory(self, senate):
        senate=list(senate)
        x=0
        while len(set(senate)) != 1:
            if x == len(senate):
                x = 0
            if senate[x] == "R":
                for offset in range(1, len(senate)):
                    idx = (x+offset) % len(senate)
                    if senate[idx] == "D":
                        senate.pop(idx)
                        if idx > x:

                            x += 1
                        break
            elif senate[x] == "D":
                for offset in range(1, len(senate)):
                    idx = (x+offset) % len(senate)
                    if senate[idx] == "R":
                        senate.pop(idx)
                        if idx > x:

                            x += 1
                        break
            
        if senate[0] == "R":
            return "Radiant"
        return "Dire"
"""
