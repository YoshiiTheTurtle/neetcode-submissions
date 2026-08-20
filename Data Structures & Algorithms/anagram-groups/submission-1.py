class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: defaultDic = defaultdict(list)
        res = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            groups[sortedWord].append(word)
        
        for group in groups.values():
            res.append(group)

        return res
        
