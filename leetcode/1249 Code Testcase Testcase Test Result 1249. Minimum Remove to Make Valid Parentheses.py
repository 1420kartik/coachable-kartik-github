class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        result = []

        # The following loop will account for all the open parentheses and matches
        # And remove all the extra close parentheses
        for char in s:
            # Keeping count of all open parentheses
            if char == '(':
                result.append(char)
                count += 1

            # If we come across close parentheses, we check if it is a match
            elif char ==')' and count > 0:
                result.append(char)
                count -= 1

            elif char != ')':
                result.append(char)

        final = []

        # The following for loop account for all the unmatched open parentheses
        # And remove it from the final
        for char in result[::-1]:

            # If we have count more than 0, that means the following open parentheses
            # has no match, and we have to remove it
            if char == '(' and count > 0:
                count -= 1

            else:
                final.append(char)

        # In the end, we will join the result and return it
        return "".join(final[::-1])
