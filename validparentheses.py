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
    
# raymond
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        left_facing = ['(', '{', '[']
        right_facing = [')', '}', ']']
        
        for char in s:
            if char in left_facing:
                stack.append(char)
            elif char in right_facing:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if (prev == '(' and char != ')') \
                or (prev == '[' and char != ']') \
                or (prev == '{' and char != '}'):
                    return False

        return len(stack) == 0