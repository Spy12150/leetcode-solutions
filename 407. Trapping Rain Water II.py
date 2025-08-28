class Solution(object):
    def trapRainWater(self, waterGraph):
        layerGraph = []
        for x in range(len(waterGraph)):
            layerGraph +=[[]]
        for x in range(len(waterGraph)):
            for y in range(len(waterGraph[0])):
                if waterGraph[x][y] > 0:
                    layerGraph[x] += [1]
                else:
                    layerGraph[x] += [0]
        return layerGraph
    
    # failed approach
    '''def measureline(self, list):
        lrlist = []
        rllist = []
        sollist = []
        value = 0
        for x in list:
            if x>value:
                value = x
                lrlist += [0]
            else:
                lrlist += [value-x]
        list.reverse()
        value = 0
        for x in list:
            if x>value:
                value = x
                rllist += [0]
            else:
                rllist += [value-x]
        rllist.reverse()
        for a in range(0,len(lrlist)):
            sollist+=[min(lrlist[a],rllist[a])]
        return sollist

    def measureHorizontal(self,hheightMap):
        for x in range(0,len(hheightMap)):
            hheightMap[x] = self.measureline(hheightMap[x])
        print(hheightMap)
        return hheightMap

    def measureVertical(self, vheightMap):
        newMap = []
        newMap2 = []
        #Mirroring map for measureline function
        print(vheightMap)
        for x in range(0,len(vheightMap[0])):
            newMap += [[]]
        for z in range(0,len(vheightMap)):
            for y in range(0,len(vheightMap[0])):
                newMap[y] +=  [vheightMap[z][y]]
        #running Measureline function
        print(newMap)
        for x in range(0,len(newMap)):
            newMap[x] = self.measureline(newMap[x])
        print(newMap)
        # Remirroring Map
        for x in range(0,len(newMap[0])):
            newMap2 += [[]]
        for z in range(0,len(newMap)):
            for y in range(0,len(newMap[0])):
                newMap2[y] +=  [newMap[z][y]]
        print(newMap2)
        return newMap2

    def trapRainWater(self, heightMap):
        print(heightMap)
        heightMap2 = heightMap
        solMap = []
        sol = 0
        print(heightMap2)
        print("^^^^^^")
        vertiMap = self.measureVertical(heightMap2)
        horiMap = self.measureHorizontal(heightMap)
        print(vertiMap)
        print(horiMap)
        for x in range(0,len(heightMap)):
            solMap += [[]]
        for x in range(0,len(heightMap)):
            for y in range(0,len(heightMap[0])):
                solMap[x] += [min(horiMap[x][y],vertiMap[x][y])]
        for x in solMap:
            sol += sum(x)
        print(solMap)
        return sol'''

Answer = Solution()
#print(Answer.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(Answer.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))