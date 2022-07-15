class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Turn list into hashtable with elem as key and index as value
        hash_table = {}
        for idx, elem in enumerate(nums):
            hash_table[elem] = idx
            
        # For each element in nums, check if the solution is in our table
        # e.g. [2,7,11,15] target = 9
        # hash-table = ["2":0, "7":1, "11":2, "15":3] 
        # solution 9 - 2 = 7   --> Check if 7 is in our table
        # 7 is in our table and has index 1
        # Thus for solution 2 + 7 = 9 we return index locations [0, 1]
        for idx, elem in enumerate(nums):
            if (target - elem) in hash_table and hash_table[target-elem] != idx:
                return [idx, hash_table[target-elem]]
            
        return []