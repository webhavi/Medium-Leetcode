class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if not  nums:
            return 0
    #nums = [ 100 , 4 , 200, 1 , 3 ,  2  ]
    #nums = [1,2,3,4,100,200]
        nums.sort()
        count = 1
        longest = 1 

        for i in range(1, len(nums)):
         #start , stop , difference 
            if nums[i] == nums[i-1]:
                continue 
            elif nums[i] == nums[i-1] +1:
             count += 1
    #nums [i] = 3
    #nums [i-1] = 2
    #nums [i-1]+1 = 3 -> a checker who checks if the element is greater or not 

            else:
             count = 1
            longest = max(longest,count) 
        return longest          
