#observations 53:   45:    11:   
#sample input: 32: 2178309  36: 14930352


def solution_station_1(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return solution_station_1(n - 1) + solution_station_1(n - 2)


print(solution_station_1(11))

