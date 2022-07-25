#  class
# 객체지향

# result = 0
# result2 =0

# def add(a,b):
#     global result
#     result = a + b
#     return result
#
# def add2(a,b):
#     global result
#     result = a * b
#     return result
#
# print(add(3,4))
# print(add2(5,6))

# class Calculator:
#     def add(self, a, b):
#         self.result = a + b
#         return self.result
#
# a = Calculator() # 객체 생성
# b = Calculator() # 더 만들고 싶을때 객체 생성
# c = Calculator()
#
# print(a.add(3,4))
# print(b.add(5,6))
# print(b.add(7,8))
#
# print(a.result)
# print(b.result)




# pass  // 아직 만들지않았을떄 pass 라고 먼저 칭해놓음
# class Myclass:
#     pass


# class Calculator:
#     def __int__(self): # 생성자
#         pass
#     def setdata(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         self.result = self.a + self.b
#         return self.result
#
#     def mul(self):
#         self.result = self.a * self.b
#         return self.result
#
#     def div(self):
#         self.result = self.a / self.b
#         return self.result
#
#     def sub(self):
#         result = self.a - self.b
#         return result


# a = Calculator()
# b = Calculator()




# a.setdata(5, 3)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
# print(a.a)
# print(a.b)
# print(a.result)
# # print(b.a)# 에러
# b.setdata(1, 2)
# print(b.a)


#
# class Calculator:
#     def __init__(self, a, b):  # 생성자
#         self.a = a
#         self.b = b
#     def __del__(self): # 소멸자
#         pass
#     def setdata(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         self.result = self.a + self.b
#         return self.result
#
#     def mul(self):
#         self.result = self.a * self.b
#         return self.result
#
#     def div(self):
#         self.result = self.a / self.b
#         return self.result
#
#     def sub(self):
#         self.result = self.a - self.b
#         return self.result
#
#
#
#
# # 생성자
# a = Calculator(4, 5)
# b = Calculator(2, 6)
# #c = Calculator()#에러
#
# print(a.add())
# a.setdata(7, 3)
# print(a.add())
#
#
# # 클래스 상속
# class Player:
#     def __init__(self, hp, attack):
#         self.hp = hp
#         self.attack = attack
#     def Move(self):
#         print(" 이동")
#
#     def Attack(self):
#         print(" 공격")
#
#
# class Knight(Player):
#     def Attack(self):
#         print(" 기사 공격")
#
#
# # 메소드 오버라이딩
# class Mage(Player):
#     def setMp(self,mp):
#         self.mp = mp
#     def Attack(self):
#         print("마법 공격")
#
#
#
# knight1 = Knight(100, 10)
# mage1 = Mage(60, 5)
# mage1.setMp(20)
#
# knight1.Move()
# print(knight1.hp)
# print(mage1.mp)
# print(knight1.Attack())
# print(mage1.Attack())


# 클래스와 객체 변수
class Myclass:
    id =0 # 클래스 변수
    def __init__(self,a):
        self.a = a # 객체 변수
    def getData(self):
        return self.a

my = Myclass(10)
my2 =Myclass(3)
print(my.id)
print(my2.id)
my.id = 10
Myclass.id = 2 # 클래스 변수 접근
print(my.id)
print(Myclass.id)






