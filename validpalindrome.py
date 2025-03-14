class Solution(object):
    def isPalindrome(self, s):
        length = len(s)
        i = 0
        j = length - 1
        lowerS = lower(s)

        while(True):
            if i >= j:
                return True

            while(True):
                if i >= length:
                    return True
                iChar = lowerS[i]
                if iChar.isalpha() or iChar.isdigit():
                    break
                i += 1
            while(True):
                if j < 0:
                    return True
                jChar = lowerS[j]
                if jChar.isalpha() or jChar.isdigit():
                    break
                j -= 1
                
            if lowerS[i] != lowerS[j]:
                return False
            i += 1
            j -= 1
                
        