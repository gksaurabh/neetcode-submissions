class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = 0
        left = len(numbers) - 1
        result = []
        
        while (len(result) == 0):
            sum = numbers[right] + numbers[left]

            if sum > target:
                left -= 1
            
            elif sum == target:
                result.append(right + 1)
                result.append(left + 1)
            else:
                right += 1

            
        return result
