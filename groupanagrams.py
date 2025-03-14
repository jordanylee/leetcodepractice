from collections import defaultdict

# jordan
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = defaultdict(list) 
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
    
# raymond 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = {}

        for s in strs:
            key = "".join(sorted(s))
            if(key not in d):
                d[key] = []
            d[key].append(s)

        return d.values()