from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agram_dict = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            agram_dict[key].append(string)
        return list(agram_dict.values())