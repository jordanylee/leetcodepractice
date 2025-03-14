class Solution(object):
    def isPalindrome(self, s):
        string = str()
        lengthS = len(s)
        for i in range(lengthS):
            char = s[i]
            if char.isalpha() or char.isdigit():
                string += char
        string = lower(string)

        length = len(string)
        j = length - 1
        for i in range(length):
            if i >= j:
                return True
            if string[i] != string[j]:
                return False
            j = j - 1
        return True