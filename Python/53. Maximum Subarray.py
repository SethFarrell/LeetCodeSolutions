class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        largest_sum = nums[0]
        curr_sum = 0
        
        for elem in nums:
            curr_sum += elem
            if curr_sum > largest_sum:
                largest_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
            
        return largest_sum