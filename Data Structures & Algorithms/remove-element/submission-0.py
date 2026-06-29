class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #remove instance of val in place 
        #return nums, first k values != val finally, return k as well (order dont matter)
        k=0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1
        return k 






        