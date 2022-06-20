class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
       
        # Iterate over the elements in the string and use
        # a dictionary to keep count of each character
        for elem in s:
            if elem in dict:
                dict[elem] += 1
            else:
                dict[elem] = 1
                
            
        # Go back over the string and see if current character
        # was only counted once (non-repeating)
        for idx, char in enumerate(s):
            if dict[char] == 1:
                return idx
            
        # If a non-repeating character was not found
        # ie every character was counted >= 2 times
        return -1