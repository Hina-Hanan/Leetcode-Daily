from sortedcontainers import SortedList
from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        def update(num, qty):
            nonlocal sb
            if freqs[num]:
                try:
                    small.remove([freqs[num], num])
                except:
                    big.remove([freqs[num], num])
                    sb -= freqs[num] * num
            freqs[num] += qty
            if freqs[num]:
                small.add([freqs[num], num])

        small, big = SortedList(), SortedList()
        freqs = Counter()
        sb = 0
        n = len(nums)

        answer = []
        for i in range(n):
            update(nums[i], 1)
            if i >= k:
                update(nums[i - k], -1)
            while small and len(big) < x:
                cx, num = small.pop()
                sb += cx * num
                big.add([cx, num])
            while small and small[-1] > big[0]:
                cx, num = small.pop()
                cy, y = big.pop(0)
                sb += cx*num - cy*y
                small.add([cy, y])
                big.add([cx, num])
            if i >= k - 1:
                answer.append(sb)
        return answer