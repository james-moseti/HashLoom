# jemo_tech@2025
# below is a O(n^2) function

def two_sum(A, target):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i]+A[j] == target:
                return [i,j]
            
nums = [7, 2, 9, 3, 11]
print(two_sum(nums, 5))
nums =[3, 3]
print(two_sum(nums, 6))
nums = [3, 2, 4]
print(two_sum(nums, 6))
