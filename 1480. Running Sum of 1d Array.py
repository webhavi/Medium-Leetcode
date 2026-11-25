class Solution:
  def runningSum(self, nums: list[int]) -> list[int]:

    Sum = 0 
    result = []
    for num in nums:
      sum += num
      result.append(sum)
    return result
   
