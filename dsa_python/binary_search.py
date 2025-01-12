# jemo_tech@2025
# below is a O(log(n)) function with constant space
# iterative approach

class Solution:
    def binary_search(self, list: list, target: int):
        first = 0
        last = len(list) - 1
        
        while first <= last:
            midpoint = first + (last - first) // 2
            
            if list[midpoint] == target:
                return midpoint
            elif list[midpoint] < target:
                first = midpoint + 1
            else:
                last = midpoint - 1
                
        return None
    

def verify(position):
    if position is not None:
        print(f"Target found at index: {position}")
    else:
        print("Target not found")


if __name__ == "__main__":   
    solution = Solution()       
    nums = [1, 2, 4, 5, 7,  8, 10, 13, 17, 21, 26, 27, 32]
    target_val = 17
    result = solution.binary_search(nums, target_val)
    verify(result)
