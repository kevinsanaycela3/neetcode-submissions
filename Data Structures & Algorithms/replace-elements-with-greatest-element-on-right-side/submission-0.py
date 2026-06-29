class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = [0] * len(arr)
        output[len(arr)-1] = -1
        max_tracker = 0
        for i in range(len(arr)-1,0,-1):
            max_tracker = max(output)
            if arr[i] >= max_tracker:
                max_tracker = arr[i]
            output[i-1] = max_tracker
        return output






            

        