import calendar

def solution_station_2 (input):
    y,m,d = map(int, input.split('-'))
    output = calendar.weekday(y,m,d)
    return output

