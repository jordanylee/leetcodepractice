#jordan 

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = list()
        for char in s:
            if char == '(' or char == '{' or char == '[':
                l.append(char)
            else:
                if len(l) == 0:
                    return False
                if char == ')':
                    if l[-1] != '(':
                        return False
                elif char == '}':
                    if l[-1] != '{':
                        return False
                elif char == ']':
                    if l[-1] != '[':
                        return False
                l.pop()
        if len(l) > 0:
            return False
        return True