class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap {unique_num : frequency_count}
        frequency_map = {}
        #unique_num = set of the nums
        for num in nums:
            if num in frequency_map.keys():
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        sorted_map = dict(sorted(frequency_map.items(), key=lambda x: -x[1])) # sort hashmap in descending order
        result = []

        for i in range(k):
            result.append(list(sorted_map.keys())[i])

        return result