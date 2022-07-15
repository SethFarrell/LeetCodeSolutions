# Go through the elements of our list and use a dictionary to track how many times we see 
# a specific element. As soon as we encounter a repeated element (duplicate) return true
# if we reach the end of the list without triggering this condition, there are no duplicates
# return false
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        
        for elem in nums:
            if elem in counts:
                return True
            else:
                counts[elem] = 1
                
        return False

# Intuition
# If the number of elements in our list are more than the number of unique elements (found via set)
# then we have duplicates in our list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_elems = len(nums)
        num_unique_elems = len(set(nums))

        return num_elems > num_unique_elems