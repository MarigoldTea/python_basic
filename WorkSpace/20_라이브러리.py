# # 시간과 날짜
import datetime
# date() : 날짜정보
# time() : 시간정보
# now() : 시스템의 현재날짜, 시간정보
# weekday() : 요일

dt = datetime.date(2022, 5, 20)
print(dt)
# 년도 ,월, 일   출력
print(dt.year, dt.month, dt.day)

dt = datetime.time(11, 10, 15, 30)
print(dt)
print(dt.hour, dt.minute, dt.second, dt.microsecond)

dt = datetime.datetime(1999, 1, 1, 10 ,13, 10)
print(dt)

dt = datetime.datetime.now()  # 현재기준  월 ,날짜,일 시간 ,초
print(dt)

print(dt.strftime("%y/%m/%d %p/ %A"))

# 달력
import calendar

print(calendar.calendar(2022))
print(calendar.calendar(2022, 5))
print(calendar.weekday(2022, 12, 31))  # 0 월, 1 화, 2 수, 3 목, 4 금, 5 토, 6일

# webbrowser
import webbrowser

webbrowser.open("google.com") # 기존에 열려있던 창에서 같이 열림
webbrowser.open_new("naver.com")  # 기존에 열려있으면 새로 열림



