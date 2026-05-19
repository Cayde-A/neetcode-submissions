from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = defaultdict(int)

        for n in nums:
            group[n] += 1

        result = sorted(
            group,
            key = lambda x: group[x],
            reverse = True
        )

        return result[:k]