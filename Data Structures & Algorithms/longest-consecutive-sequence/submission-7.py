class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert our list to a set
        nums_set = set(nums)
        longest = 0 # keep track of a longest count

        # ittereate through our array
        # check if n - 1 is not in our set, means we have encountered a start of a possible longest sequence
        # then you set the length to 0 
        # keep checking if (n + length) is in our set and increment our length if it is. 
        # set longest to the max value between longest and length
        
        for n in nums:
            if (n - 1) not in nums_set:
                length = 0
                while (n + length) in nums_set:
                    length += 1
                longest = max(length, longest)
        
        return longest

