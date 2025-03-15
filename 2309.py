# jordan time 33.33 memory 91.23

class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        ascii_val_A = ord('A')
        ascii_val_a = ord('a')

        lowerChars = [0] * 26
        upperChars = [0] * 26
        greatest_letter = ""
        for char in s:
            if char.isupper():
                upperChars[ord(char) - ascii_val_A] += 1

                if lowerChars[ord(lower(char)) - ascii_val_a] == 0:
                    continue
                if char > greatest_letter:
                    greatest_letter = char
            else:
                lowerChars[ord(char) - ascii_val_a] += 1

                if upperChars[ord(upper(char)) - ascii_val_A] == 0:
                    continue
                if upper(char) > greatest_letter:
                    greatest_letter = upper(char)

        return greatest_letter
    

# raymond time 43.86 memory 57.89
class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        greatest_letter = ""
        for char in s:
            if char.islower() and char.upper() in s:
                greatest_letter = max(greatest_letter, char.upper())
        return greatest_letter