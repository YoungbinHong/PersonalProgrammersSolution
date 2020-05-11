import calendar

def solution(month,day):
    day_of_the_week = calendar.weekday(2016,month,day)
    return calendar.HTMLCalendar.cssclasses[day_of_the_week].upper()

print(solution(5,24))
