class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the nums into set, so the look up time is constant
        nums = set(nums)

        # Set current observed longest streak to 0
        longest_streak = 0

        # Iterate over the nums set
        for number in nums:

            # Check if there a consecutive smaller number there in the nums
            # If present, do not update the streak. Else, continue
            if number-1 not in nums:
                current_streak = 1

                # Check if there are cosecutive numbers present in nums, and update streak accordingly
                while number+1 in nums:
                    current_streak += 1
                    number += 1

                longest_streak = max(current_streak, longest_streak)

        # Return the longest streak observed        
        return longest_streak
