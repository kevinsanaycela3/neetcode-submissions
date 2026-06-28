class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for element in nums:
            if element in tracker:
                tracker.update({element: tracker[element]+1})

            else:
                tracker.update({element: 1})

        sorted_tracker = sorted(tracker, key=tracker.get, reverse=True)

        return(sorted_tracker[:k])