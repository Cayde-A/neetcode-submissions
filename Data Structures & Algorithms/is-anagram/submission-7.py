class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        current = ''
        return Counter(s) == Counter(t)
