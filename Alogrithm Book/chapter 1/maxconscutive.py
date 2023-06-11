#sliding window approach 
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        maxones = 0 
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxones = max(maxones, right-left + 1)
        return maxones
      
      """Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined."""
