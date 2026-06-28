class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tracker = []
        count = 0
        for element in nums:
            if element == 1: 
                count = count + 1
                tracker.append(count)
            else:
                tracker.append(count)
                count = 0
        return max(tracker)