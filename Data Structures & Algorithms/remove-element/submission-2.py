class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # set our k pointer
        k = 0
        
        # itterate through the list
        for i in range(0,len(nums)):

            # if we don't find a matching value, then swap value with k pointer and increment k 
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
        return k