class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output = []
        n = len(heights)

        # We will iterate over the heights of buildings and upte the output accordingly
        for i in range(n):

            # At every iteration, we will check if the height of the current building is taller or equal to the last building in the output
            # If true, we will pop that building from the output
            while output and heights[i] >= heights[output[-1]]:
                output.pop()

            # We will add the index of the current building to our output
            output.append(i)

        return output
