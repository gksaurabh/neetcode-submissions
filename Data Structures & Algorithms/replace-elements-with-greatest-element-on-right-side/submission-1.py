class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # our initalmax is -1 
        rightMax = -1

        # itterate backwards to the array 
        for i in range(len(arr) - 1, -1, -1):
            # we take the max value between the current element and the rightMax from the previous itteration
            newMax = max(rightMax, arr[i])

            # we set the current element to the rightMax
            arr[i] = rightMax

            # we reassign the rightMax based on the newMax function
            rightMax = newMax
        return arr