"""
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets.
To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
If it is impossible to make m bouquets return -1.
"""


class Solution:
    def calculate(self, bloomday, m, k, mid):
        count = 0
        bouquet = 0
        for value in bloomday:
            if value > mid:
                count = 0
            else:
                count += 1
                if count == k:
                    bouquet += 1
                    count = 0
        return bouquet >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)

        ans = 99999999999999
        while low <= high:
            mid = low + (high - low) // 2
            if self.calculate(bloomDay, m, k, mid) == True:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans
