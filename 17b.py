def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        temp = 0
        length = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if height[i] > height[j]:
                    length = i - j
                    length = abs(length)
                    if temp < height[j] * length:

                        temp = height[i] * height[j]
                        print(temp)
                        print(i,j)
                        print(height)
                elif height[j] >= height[i]:
                    length = i - j
                    length = abs(length)
                    
                    if temp < height[i] * length:
                        temp = height[i] * length
                        
        return temp

print(maxArea([1,8,6,2,5,4,8,3,7]))