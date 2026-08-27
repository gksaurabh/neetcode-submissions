class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            duplicateCount = 0
            for i in range(0,len(nums)):
                if num - nums[i] == 0:
                    duplicateCount += 1
            if duplicateCount > 1:
                return True
        return False