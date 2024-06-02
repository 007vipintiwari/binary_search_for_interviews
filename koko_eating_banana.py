"""
https://leetcode.com/problems/koko-eating-bananas/
Koko loves to eat bananas.
There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""


class Solution(object):
    def time_needed_to_eat_bananas(self, piles, mid):
        time = 0
        for banana in piles:
            if banana % mid == 0:
                time += banana / mid
            else:
                time += banana / mid + 1

        return time

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        ans = 99999999999999999
        while low <= high:
            mid = low + (high - low) // 2
            value = self.time_needed_to_eat_bananas(piles, mid)
            if value <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans
