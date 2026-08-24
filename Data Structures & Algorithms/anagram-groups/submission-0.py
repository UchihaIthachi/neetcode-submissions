from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        inx = {}
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            if key in inx:
                lst[inx[key]].append(s)
            else:
                inx[key] = len(lst)
                lst.append([s])
        return lst