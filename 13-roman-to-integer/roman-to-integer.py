class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        # Example: IV, then split into [I, V] -> I = 1 + V = 5
        # Since s[0] < s[1], then the formula is s[1] - s[0]

        # "MMM"
        # 1. s[2] = 1000. Is s[2] (1000) > s[1] (1000)? No, so we add the value s[2] and s[1] to the result, then we move two steps backward
        # 2. s[1] = 

        r = 0
        while r < len(s):
            left = roman[s[r]]
            if r != len(s)-1:
                right = roman[s[r+1]]
            else:
                result += left
                break
            
            if left < right:
                result += (right-left)
                r+=1
            else:
                result += left
            r+=1
        return result



        