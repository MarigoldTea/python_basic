# 산술 연산자
a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b) # 나누기
print(a%b) # 나머지
print(a**b) # 제곱
print(a//b) # 몫

# 연산자 우선순위 ( 위에서 부터 우선시 됨)
# **
# * , / , // , %
# +, -


a =  10 + 2 - 3 * 2 ** 2
print(a)

# 반지름이 5인 원의 면적을 구하시오

a = 5 ** 2 * 3.14
print(a)

# 입력
# a = float(input('소수점 :  '))
# print(a)


# 반지름을 입력받아 원의 면적을 구하시오

# a = int(input("반지름 입력 : ")) # input 으로 넘어온 값은 Str (문자열) 이다
# result = a ** 2 * 3.14
# print(result)

# 대입연산자
a = 5 # '=' 도 하나의 대입연산자
b = 3

a += b # a = a + b
a -= b # a = a - b
a *= b
a /= b
a **= b
a %= b
a //= b
print(a)

# 관계연산자
a = 3
# b = 5
#
# b = a >  0
# print(b)
# b = a <  0
# print(b)
# b = a >= 0
# print(b)
# b = a <= 0
# print(b)
# b = a == 0
# print(b)
# b = a != 0
# print(b)

# b = 0 < a <10 # a가 10보다 작고 0 보다 큰가?
# print(b)

# 논리 연산자
# and(논리곱) - 둘다 참일때만 참 이고 나머지는 거짓
# 1010
# 1100
# ----
# 1000

# or (논리합) - 둘중에 참이면 참
# 1010
# 1100
# ----
# 1110

# xor(배타적논리합) - 다르면 참, 같으면 거짓
# 1010
# 1100
# ----
# 0110


# not
# 1010
# 1100
# ----
# 0101


from operator import xor
a = 5
b = 3
result = a > 0 and b < 0 # 1과 0 : 둘다 참일때만 참 그렇지않으면 거짓
print(result)
result1 = a > 0 or b < 0 # 둘중에 하나라도 참이면 참
print(result1)
result2 = not (a > 0) #   참 이니까 반대로 거짓을 반환
print(result2)
result3 = xor(a > 0 , b < 0) #  둘이 다르면 참 같으면 거짓
print(result3)

# 비트 연산자
# << 왼쪽 쉬프트 연산자
# >> 오른쪽 쉬프트 연산자
# & :and
# | :or
# ^ : xor
# ~ : not

a = 2 & 1
print(a)
a = 2 | 1
print(a)
a = 2 ^ 1
print(a)
a = ~(2)
print(a)
a = 2 << 3 # 왼쪽으로 3칸
print(a)
a = 2 >> 1 # 오른쪽으로 1칸
print(a)

# 음수
# 0000 0010
# 1111 1101 # 1의 보수
# 1111 1110 # 2의 보수

# 1111 1110 # -2
# 0000 0001 # 1


a = -2 & 1
print(a)
a = -2 | 1
print(a)
a = -2 << 1
print(a)
a = -2 >> 1
print(a)


# 구성원연산자
# in
# not in

a = "hello World"
print("hello" in a) # hello 가 a 변수 안에 존재하는가?
print("hello" not in a)  # hello 가 a 변수안에 존재하지않는가? : 존재하니 거짓
a = [1,2,3,4]
print(2 in a)


# 식별 연산자
# is
# is not
a = 10
b = 10
print(a is b)
print(a is not b)
