#문자열 (String) - 문자 , 단어 등으로 구성된 문자들의 집합

a = "안녕하세요 파이썬"
b = '안녕하세요 파이썬'
c = """안녕하세요 파이썬"""
d = '''안녕하세요 파이썬'''
print(a)
print(b)
print(c)
print(d)

# 문자열에 따옴표(') 포함할때
e= "Python's"
print(e)
# 문자열에 쌍다옴표(") 포함할때
f = 'python"hello"' # "hello" 를 " 로 묶어서 출력하고싶을때 ' 를 사용
print(f)

# 이스케이프 코드 사용
g = 'python\'s'
print(e)
h = "hello\"python\""
print(h)

j = "hello\nWorld"
print(j)

t = "hello\tworld"
print(t)

# 여려줄 문자열
n = """hello
world"""
print(n)

print(type(a))

# 문자열 연산
a = "hello"
b = "World"
c= a + b
print(c)

d = a * 3 # hello 를 3번 출력
print(d)

e = a + str(3)
print(e)


# 문자열 길이
print(len(b))

# 인덱싱
a = "동해물과 백두산이 마르고 닳도록"
print(a[3])
print(a[10])
print(a[-1])
print(a[-3])


# 슬라이싱 [시작 :끝 -1:증가치]
b = "동해물과 백두산이 마르고 닳도록"
print(b[5:8])
print(b[:6])
print(b[5:])
print(b[12:-2])
print(b[::2])

#슬라이싱 문자열 나누기
b = "20220515rain"
Date = b[:8]
weather = b[8:12]
print(Date)
print(weather)

# 문자열 바꾸기 는 안된다
# immutable(값이 변하지않음)  자료형
a = "동해물과 백두산이 마르고 닳도록"
print(a[0])
#a[0] = "서" # 에러

# 문자열 포맷팅 ( 첫번째 방법 )
# %d는 정수
# %s는 문자열
# %f 실수
number = 20
a = "현재 %10s는 %d도 입니다" % ("온도",number)
b = "현재 %-10s는 %d도 입니다" % ("온도",number)
print(a)
print(b)


a = "%10.3f" % 3.1415
print(a)

# 문자열 포맷팅 ( 두번째 방법 )
a = "현재 {0}는 {1}도 입니다" .format("온도",20)
print(a)
a = "현재 {0}는 {number}도 입니다" .format("온도", number = 20)
print(a)


# 문자열 포맷팅 ( 세번째 방법 ) // 가장 최근에 나온 방식
a = f"현재 온도는 {number + 2}도 입니다"
print(a)


# 문자열 관련 함수들

# 문자 갯수 세기 (count)
a = "hello"
print(a.count("l")) # l 의 갯수

# 문자 위치 알려주기 (find) 없으면 -1 반환
a = "python"
print(a.find("h"))

# 문자 위치 알려주기 2 (index) : 없으면 에러 출력
print(a.index("h"))


# 문자열 삽입 (join)
a = "hello"
a= " ".join(a)
print(a)

# 소문자를 대문자로
a = "hello"
print(a.upper())


# 대문자를 소문자로
b = "HELLO"
print(b.lower())

# 공백 지우기
a = "    python    "
print(len(a))
#a = a.lstrip() # 왼쪽 공백 지우기
#a = a.rstrip() # 오른쪽 공백 지우기
a = a.strip()  # 양쪽 공백 지우기
print(a)

# 문자열 바꾸기 (replace)
a = "python"
print(a.replace("p" , "f"))

# 문자열 나누기 (split)
a = "do,it"
b= a.split(",") # 안적으면 기본 공백
print(b)

print(b , type(b))


