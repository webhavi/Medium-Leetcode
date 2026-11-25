class Solution:
    def containsDuplicate(self, nums):

     seen = set()

     for num in nums:
      if num is seen:
        return True
        seen.add(num)
     return False
        
