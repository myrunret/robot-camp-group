#observations 53:   45:    11:   
#sample input: 32: 2178309  36: 14930352


def solution_station_1(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(solution_station_1(11))
    
