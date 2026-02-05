class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tom=[0]*26
            for char in s:
                tom[ord(char)-ord('a')]+=1
            key=tuple(tom)
            res[key].append(s)
        return list(res.values())
        