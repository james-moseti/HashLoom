# jemo_tech@2025
# below is a O(n) function
from typing import List, Optional


class Solution:
    def linear_search(self, A: List[int], target: int) -> Optional[int]:
        """
        Returns the index position of the target if found, else returns None
        """

        for i in range(len(A)):
            if A[i] == target:
                return i
            
        return None

def verify(position):
    if position is not None:
        print(f"Target found at index: {position}")
    else:
        print("Target not in list")

solution = Solution()
nums = [2, 4, 5, 23, 42, 12, 24, 8, 32, 16]
 
target_val = 5
result = solution.linear_search(nums, target_val)
verify(result)