class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            first = nums[i]
            for j in range(0, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
                
        
        