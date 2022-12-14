# Min Steps to Make Piles Equal Height
#
# Alexa is given n piles of equal or unequal heights. In one step,
# Alexa can remove any number of boxes from the pile which has the maximum
# height and try to make it equal to the one which is just lower than the
# maximum height of the stack. Determine the minimum number of steps required
# to make all of the piles equal in height.
#
# Example 1:
# Input: piles = [5, 2, 1]
# Output: 3
# Explanation:
# Step 1: reducing 5 -> 2 [2, 2, 1]
# Step 2: reducing 2 -> 1 [2, 1, 1]
# Step 3: reducing 2 -> 1 [1, 1, 1]
# So final number of steps required is 3.
class Solution(object):
    def minStepsBalance(self, piles):
        sorted_unique_piles = sorted(set(piles), reverse=True)
        piles_count = []
        for p in sorted_unique_piles:
            piles_count.append(piles.count(p))

        answer = 0
        last_index = len(sorted_unique_piles) - 1
        for i in range(last_index):
            answer += piles_count[i] * (last_index - i)

        return answer
