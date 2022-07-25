# 함수


# #def 함수이름(매개변수):
#     함수내용
#     함수내용
#     return 리턴값

# 입력 값 이 없는 함수
def hello():
    return "world"
a = hello()  # world 를 담아놓음

print(hello())

# 출력 값 이 없는 함수
def add(a,b):
    print(f"{a} + {b} = {a+b}")
add(3,5)


# 입력값 , 출력값 도 없는 함수
def world():
    print("hello world")
world()

def mul(a,b):
    return a * b
print(mul(4 , 3))


# 매개변수 를 지정해서 호출
def div(a,b):
    return a / b
result = div (a = 5 ,b =3)
print(result)

# 입력값(매개변수) 가 여러개 일때 // 가변매개변수
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
print(add_many(1,4,5,6,7,10,30))

def Cal(select, *agrs):
    if select == "add":
        result = 0
        for i in agrs:
            result += i
    elif select == "mul":
        result = 1
        for i in agrs:
            result *= i
    return result
print(Cal("add",1,2,3,4,5,4,5))

# 키워드 파라미터 (kwargs)
def kwfunc(**kwargs):
   return kwargs

a = kwfunc(name="홍길동" ,age =26, phone = "123456")
print(a)

# 함수는 출력 값이 하나이다.
def Calcula(a,b):
    return a + b
#   return a * b  # 리턴이 있으면 실행하고 종료시킴
print(Calcula(3,4))

def Calcula2(a,b):
    return a + b , a * b
print(Calcula2(3,4))

# return 의 다른 쓰임새
def func1(a):
    if a < 0:
        return
    print(a)
func1(-1)

# 매개변수 디폴트 값
def fucn2(a,b = 0):
    return a + b
print(fucn2(3,4))


# # 잘못 된 디폴트 값 예
# def fucn3 (a = 0 , b): # a = 0 부분이 뒤로 와야됨
#     return a + b
# fucn3(3)



# 변수의 범위
# a = 10 # 전역 변수 (글로벌 (global) )
#
# def func():
#     a = 100 # 지역 변수
#
# func()
# print(a)

# 함수 안에서 함수밖의 변수를 변경하는 방법
# return 을 이용하는 방법
# a = 10
# def func():
#     a = 100
#     return a
#
# a = func()
# print(a)

# global 키워드 이용하는 방법
# a = 10
# def func():
#     global a
#     a = 100
#
# func()
# print(a)

#  함수의 참조
# def func():
#     print("hello world")
# a = func
#
# a()

# 함수의 매개변수에 함수 이름으로 인자를 넘김
# def fn():
#     print("hello world")
# def my(a):
#     a()
# my(fn)

# def fn():
#     print("hello world")
# def my():
#     return fn()
# a= my()



# 람다 lambda
add = lambda a, b : a + b  # a,b 입력 : a + b 출력
result = add(3,4)
print(result)

# 위에랑 같은 말임
# def add(a,b):
#     return  a+ b
#
# result = add(3,4)
# print(result)











