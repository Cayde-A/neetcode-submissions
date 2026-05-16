class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        current = ''
        return sorted(s) == sorted(t)
