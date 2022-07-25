# while 문 (반복문)
# 초기값 , 조건식, 증감

# a = 0
#
# while a < 10:
#     print("?")
#     a +=1

# break
# a = 0
# while a < 10:
#     if a == 3:
#         break
#     print(a)
#     a += 1
#
#
# # else
# while a < 10:
#     # if a == 3:
#     #     break
#     print(a)
#     a += 1
# else:
#     print("else")
#
# # 합계
# n = 1
# sum = 0
#
# while n <= 10:
#     print(n)
#     sum += n
#     n += 1
# print("합계 :", sum)


# import random
# com = random.randint(1, 3)
# player = 0
#
# while True:
#     player = input("입력 : ")
#     player = int(player)
#     if (player >= 1) and (player <= 3):
#         break
#
# if player == 1:
#     print("당신은 가위")
# elif player == 2:
#     print("당신은 바위")
# elif player == 3:
#     print("당신은 보")
# else:
#     print("이상한 값입니다")
#
# if com == 1:
#     print("컴퓨터는 가위")
# elif com == 2:
#     print("컴퓨터는 바위")
# else:
#     print("컴퓨터는 보")




# 출력

# print("hello", end ="\t" )
# print("hello","world", sep="")


# for 문
#  for 변수 in 반복가능데이터:
#      수행문장
#      수행문장



# a= [1,2,3,4,5]
#
# for i in a:
#     print(i)



# 리스트안에 튜플

# a = [(1,2) , (3,4) , (5,6)]
# for i,j in a:
#     print(i,j)


# 튜플

# a = ( 1, 2, 3, 4, 5)
# for i in a :
#     print(i)


# 세트

a = {1,2,3,4,5}
for i in a :
    print(i)


# 딕셔너리

a = {1:'a', 2:'b', 3:'c'}
for i,j in a.items():  #  키 값만 나옴 value 려면 'a.values()' 입력
    print(i,j)


# 시험을 친 사용자(key)명과 점수(value)
score = {'홍길동': 80, '황길동': 30, '김길동': 25, '고길동': 48, '이길동': 65, '최길동': 100, '박길동': 37, '조길동': 55}

# 합격자 수
count = 0
# 합계 점수
sum = 0

# key 값은 name변수로, value 값은 jumsu변수로 불러옴
for name, jumsu in score.items():  # 딕셔너리 items 사용 키와 값 쌍으로 가져옴
   
    sum += jumsu  # 합계에 가져온 jumsu값 추가

    if jumsu >= 60:   # 가져온 jumsu값이 60점 이상일 경우
        # 합격값 출력
        print(f"{name}은 {jumsu} 점으로 합격입니다.")  # f 포맷팅

        count += 1   # 합격자 수 추가

    else:  # 가져온 jumsu값이 60점 미만일 경우

        print(f"{name}은 {jumsu} 점으로 불합격입니다.")   # 불합격값 출력
else:

    print(f"합격자수: {count} 명 , 전체평균 : {sum / len(score)}")   # 전체 합격자 수와 평균 수 출력


# range 함수
a = range(10)
print(a, type(a))

for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

score = [30,70,50,90,25]
for i in range(len(score)):
    if score[i] >= 60:
        print(f"{score[i]}점은 합격입니다")

# 다중 for 문

for i in range(10):
    for j in range(10):
        print(i,j)

# 구구단 출력
dan = 2
for dan in range(2,10):
    for su in range(1,10):
        print(f"{dan} * {su} = {dan*su}")


# break

for i in range(10):
    if i == 5:
        break
    print(i)

# continue

for i in range(1,10):
    if i == 5:
        continue
    print(i)


# 짝수만 출력

for i in range(1,10):
    if i % 2== 1:
        continue
    print(i)



# 축약 내장 리스트
# a = [i * 3 for i in range(1,10)]
# print(a)

a = [i for i in range(1, 10) if i % 2 == 0]
print(a)
