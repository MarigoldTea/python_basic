#  내장함수
#
# print()
# del()
# type()
# id()


# abs 절대값  // 음수를 넣으면 양수 양수를 넣으면 양수

print(abs(2))
print(abs(-2))


# all
# 반복가능한 자료형 안에 있는 요소들이 모두 참이면 참
# 거짓이 하나라도 존재하면 거짓
a = [1,2,3,4,5]  # 참
print(all(a))

a = [1,2,3,4,0]  # 거짓
print(all(a))

a = [1,True,3,"aaa",[]] # 거짓
print(all(a))


# any
# 반복가능한 자료형 안에 있는 요소들이 하나라도 참이면 참
# 아니면 거짓
a = [1,True,3,"aaa",[]]
print(any(a))


# chr
# 유니코드 값 을 입력 받아 그 코드에 해당하는 문자를 출력
# print(chr(0xAC00))

# ord
# 문자를 입력받아 유니코드로 출력
print(ord('가'))


# dir
# 객체가 가지고 있는 변수나 함수를 보여준다
# print(dir([1,2,3]))


# divmod
# print(divmod(6,4)) # 몫 , 나머지  // 두개의 숫자를 입력받아 몫과 나머지를 튜플로 출력


# enumerate
# mutable 자료형의 인덱스와 값을 반환
# for i,y in enumerate(["a","b","c"]):
#     print(i,y)


# eval
# 실행 가능한 문자열을 입력 받아 실행 후 출력
print(eval('1+2'))
print(eval('divmod(4,3)'))

# hex
# 16진수 변환
print(hex(234))

# oct
# 8진수 변환
print(oct(234))

# id
# 객체의 고유 주소값(레퍼런스) 를 반환
# print(id(3))


#int , float , str

# isinstance
# 클래스의 객체인지 판별하는 함수
class Myclass:
    pass

a = Myclass()
b = 3

print(isinstance(a, Myclass))    # 앞에 객체 뒤에 클래스

# len
# 요소의 전체 갯수
print(len("abcdefg"))
print(len([1,2,3,4,5,6,7]))

# max , min
# 최대값, 최소값 구함
a = [1,2,3,4,5]
print(max(a))
print(min(a))

# sum(합계)
print(sum([1,3,4]))
# 평균
a = [1,2,3,4,5]
print(sum(a) / len(a))
# 넘파이 평균
import numpy as np
print(np.mean(a))

# round
# 반올림
print(round(123.12345, 1))

# sorted
# 정렬
print(sorted([1,6,5,2,3])) # sorted 는 정렬 하면서 반환해줌
print(a.sort())  # 반환 안해줌
print(a)  # 찍어서 출력해줘야댐

# zip
# 동일한 갯수로 이루어진 자료형을 묶어주는 역할
print(list(zip([1,2,3], [4,5,6], ['a','b','c']))) # 튜플로 묶어서 리스트로 출력됨
print(list(zip('abc','qwe')))












