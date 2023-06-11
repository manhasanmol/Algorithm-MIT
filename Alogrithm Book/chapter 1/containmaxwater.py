class Solution:
    def maxArea(self, height):
        if len(height) > 1:
            max_area = 0
            left = 0
            right = len(height) - 1

            while left < right:
                current_height = min(height[left], height[right])
                current_width = right - left
                current_area = current_height * current_width

                max_area = max(max_area, current_area)

                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1

            return max_area
        else:
            return height[0]
          
"""Input: height = [1,8,6,2,5,4,8,3,7]Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of
water (blue section) the container can contain is 49."""
