class Solution:
    def findNumbers(self, nums: list[int]) -> int:

        count = 0 

        for num in nums:

            s = str(num)
            if len(s) % 2 == 0:
             count += 1 
            else:
             continue 
        return count       
