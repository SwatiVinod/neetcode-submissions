class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        dict1 = dict()
        result = []

        for num in nums:
            dict1[num] = 1 + dict1.get(num, 0)
        
        for num, freq_val in dict1.items():
            freq[freq_val].append(num)
        
        for i in range(len(freq)-1, 0, -1):
            if len(freq[i]) > 0:
                result.extend(freq[i])
                if len(result) == k:
                    return result
        return result