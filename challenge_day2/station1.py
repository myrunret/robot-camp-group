#observations 53:   45:    11:   
#sample input: 32: 2178309  36: 14930352

def solution_station_1(n):
    #base cases
    if n==0:return 0
    if n == 1:return 1

    a,b = 0,1

    for i in range(2, n+1):
        a,b = b, a+b 
        return b


print(solution_station_1(53))
print(solution_station_1(45))
print(solution_station_1(11))
print(solution_station_1(32))
print(solution_station_1(36))    
