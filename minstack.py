# jordan 70.53 18.88

class MinStack(object):

    def __init__(self):
        self.stack = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            minimum_val = float('inf')
        else:
            minimum_val = self.stack[-1][1]
            
        if val < minimum_val:
            minimum_val = val
        self.stack.append((val, minimum_val))

    def pop(self):
        """
        :rtype: None
        """
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()