# 변수
# 파이썬에서는 모든것들이 객체로 구현
# 변수에는 값이 아닌 객체의 주소를 저장

a = 123
print(a, type(a))
a= str(a)
print(a, type(a))
str = 1234
print(str, type(str))
# b = str(str) # 오류






# a = 10
# b = 10
#
# print(a, id(a))
# print(b, id(b))
#
# b= 11
#
# print(a, id(a))
# print(b, id(b))

# a = [1,2,3]
# b = a  # a 의 주소값을 b 에 넘겨줌
#
# print(a, id(a))
# print(b, id(b))
#
# print( a is b) # a와 b 가 가리키는 객체가 같은가?
#
# a[1] = 10 # a 만 바꾸었는데 b 도 바뀜 따라서 같은 메모리 를 가리키고있는게 확인이 되는셈
#
# print(a, id(a))
# print(b, id(b))

print('=' * 50)

# mutable(변경가능) - list , dict ,set
# immutable(변경 불가능) - tuple , Str , int ,float , bool

a = [1, 2 ,3]
b = [1, 2 ,3]
# 메모리 공간을 따로따로 생성


# 얕은 복사
import copy
a = [1, 2, 3, [10, 20]]
b = a[:]
a[3][0] = 100
print(a[3], id(a[3]))
print(b[3], id(b[3]))


c = [1, 2, 3, 4]
d = copy.copy(c)

print(a, id(c))
print(b, id(d))


# 깊은 복사

a = [1, 2, 3, [10, 20]]
b = copy.deepcopy(a)

a[3][1] = 100000

print(a[3], id(a[3]))
print(b[3], id(b[3]))






# 타 언어 에서는 이런 형식으로 사용함 보통
a = b = 100

a = 3
b = 5

temp = a # 임의로 temp에다가 a 를 저장
a = b
b = temp

print(a, b)


# 파이썬에서는 이런식으로 씀
a = 5
b = 3

a,b = b,a
print(a,b)

# 변수 선언 방식
a = 3
a, b = (1, 2)
a, b = 3 , 5
(a, b) = 1 , 2
[a, b] = [1 , 2]

