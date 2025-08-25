class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        dictmap = {"2":["a",'b','c'],"3":["d",'e','f'],"4":["g",'h','i'],"5":["j",'k','l'],"6":["m",'n','o'],"7":["p",'q','r','s'],"8":["t",'u','v'],"9":["w",'x','y','z']}
        

        def recursion(string,remaining_digits,dictmap,answerlist):
            if len(string) == len(digits):
                answerlist += [string]
                return 
            else: 
                    for x in dictmap[remaining_digits[0]]:
                        new_string = string+x
                        recursion(new_string,remaining_digits[1:],dictmap,answerlist)
        answerlist = []
        recursion("",digits,dictmap,answerlist)
        return answerlist


x = Solution()
print(x.letterCombinations("2"))

# this was fucking rough btw
# I realize I don't actually know how to do recursion

