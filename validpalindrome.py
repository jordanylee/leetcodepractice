# jordan
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
                
# raymond    
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(" ", "")
        start = 0
        end = len(s) - 1

        while(start < end):
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            start += 1
            end -= 1

        return True
