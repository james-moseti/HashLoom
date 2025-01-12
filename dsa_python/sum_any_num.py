# jemo_tech@2025

def sum_num(n: int):
    if n == 0:
        return 0
    else:
        return n + sum_num(n - 1)
    
print(sum_num(5))