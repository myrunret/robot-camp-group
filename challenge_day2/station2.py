import calendar

def solution_station_2 (input):
    y,m,d = map(int, input.split('-'))
    weekday = calendar.weekday(y,m,d)
    kanji = ['月','火','水','木','金','土','日']
    output = kanji[weekday] + "曜日"
    return output

