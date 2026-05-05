class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        

        for s in strs:
            alp = [0]*26
            for c in s:
                alp[ord(c) - ord('a')] += 1
            freq[tuple(alp)].append(s)
        return list(freq.values())