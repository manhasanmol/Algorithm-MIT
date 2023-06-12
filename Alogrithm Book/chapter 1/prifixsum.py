#prifix sum
#To find the highest altitude reached during the road trip, we can calculate the cumulative sum of altitudes using the given gain array. We start with an initial altitude of 0 and add the net gain in altitude at each point to the previous altitude.
class Solution:
    def largestAltitude(self, gain):
        max_altitude = 0
        current_altitude = 0
        
        for net_gain in gain:
            current_altitude += net_gain
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude

sol = Solution()
gain = [-5, 1, 5, 0, -7]
result = sol.largestAltitude(gain)
print(result)  # Output: 1
