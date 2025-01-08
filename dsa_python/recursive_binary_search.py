# jemo_tech@2025

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else: 
        midpoint = (len(list) // 2)
        
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)
            

def verify(result):
    print(f"Target found: {result}")
    
    
nums = [x for x in range(15)]
result = recursive_binary_search(nums, 10)
verify(result)