class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        freq = [[] for i in range(len(nums) + 1 ) ]
        res = []

        #count number times each numbers shows up 
        for num in nums: 
            count[num] = 1 + count.get(num, 0)

        for key, value in count.items():
            freq[value].append(key)

        for i in range(len(freq) -1, 0, -1):
            for key in freq[i]:
                res.append(key)
                if len(res) == k:
                    return res
             


         



        
      