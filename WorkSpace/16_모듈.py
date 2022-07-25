# 모듈
# 함수나 변수 또는 클래스를 모아놓은 파일

# print(dir(__builtins__)) # 내장 함수

# import Mod1
#
# print(Mod1.add(3,4))
# print(Mod1.add(5,1))

# from Mod1 import add,sub
#
# print(add(3,4))
# print(add(5,3))
#
#
# from Mod1 import *
# print(add(3,4))
# print(add(5,3))

# import Mod1
# print(Mod1, __name__) # __name 변수


# 클래스나 변수를 포함한 모듈

import Mod1

print(Mod1.pi)

a = Mod1.Math()  #  객체 생성
print(a.solv(5))

# Path
# 모듈을 찾기위한 경로
import sys
print(sys.path)

# 새로운 경로 등록
sys.path.append("C:\\Intel")
print(sys.path)
