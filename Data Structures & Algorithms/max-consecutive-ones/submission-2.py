class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tracker = 0
        count = 0
        for element in nums:
            if element == 1:
                count = count + 1
                tracker = max(count, tracker)
            else:
                count = 0
                tracker = max(count,tracker)
        return tracker

        