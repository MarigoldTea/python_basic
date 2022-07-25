# 시퀀스 데이터 타입
# 리스트, 튜플 , 딕셔너리 , 세트


# 순서 있는 데이터 타입 (인덱싱, 슬라이싱)
# ㄴ 문자열 , 리스트 ,튜플


# 순서 없는 데이터 타입
# ㄴ 딕셔너리, 세트

# 변경가능 (mutable) 데이터타입
# ㄴ 리스트 ,딕셔너리 , 세트

# 변경불가능 (Immutable) 데이터타입
# ㄴ 문자열, 튜플

a = list()
b = []
c = [1,2,3]
d = ["a", "b" , "c ", "d"]
e = ['a' , 10 , 3.14]
f = [10,['a','b']] # 리스트 안에 리스트가 들어감
print(a , type(a))
print(b , type(b))
print(c , type(c))
print(d , type(d))
print(e , type(e))
print(f , type(f))


# 인덱싱
a = [1, 2, 3]
print(a[0], type(a[0]))
print(a[-1])
print(a[1] + a[2] )

a = [1,2,3, ['a','b','c',[10,20,30]]]  # ['a','b','c'[10,20,30]] 부분이 3에 해당함
print(a[3][3][1])


# 슬라이싱
a = [1,2,3,4,5]
print(a[:3])


# 특정한 출력값 슬라이싱 문제

a = [1,2,3, ['a','b','c'],4,5]
print(a[3][:2])
# 답:  ['a' ,'b']

# 리스트 연산
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a *3)

# 리스트 길이 구하기
a = ['python' , 'hello' , 'world']
print(len(a))


# 리스트 수정
a = [1,2,3,4,5]
a[2] = 10
print(a)


# 리스트 삭제
a = [1,2,3,4,5]
del(a[3]) # del a[3] 으로 써도 출력은 값음
print(a)
print(a[3]) # 4가 삭제 되어 5가 앞으로 땡겨와짐
del(a[0:2])
print(a)

print('-------------------------------')

# 리스트 추가
a.append(4)
print(a)
a.append([10,20])
print(a)


# 리스트 정렬
a = [3,4,1,2,5]
a.sort() # 오름차순
print(a)

b = ['c','a','d','b']
b.sort()
print(b)

a.sort(reverse=True) # 내림차순
print(a)

b = ['c','a','d','b']
b.sort(reverse=True)
print(b)

print('----------------------------------')

# 리스트 뒤집기
a= ['c','a','d','b']
a.reverse()
print(a)

print('-------------------------------------')

# 위치 반환 (index)
a = [1,2,3,4,5]
print(a.index(4)) # 4의 위치 반환


print('------------------------------------')

# 리스트 요소에 삽입 (insert)
a = [1,2,3,4,5]
a.insert(0,10) # 0을 넣으면 맨앞에 10 이 들어감
print(a)


# 리스트 요소 제거 (remove)
a= [1,2,3,4,5]
a.remove(5)
print(a)


# 리스트 요소 꺼내기 (pop)
# 리스트의 맨 마지막 요소를 돌려주고 삭제
a = [1,2,3,4,5,2]
b = a.pop(5)
print(b)
print(a)
b = a.pop(3)
print(b)
print(a)

print('-----------------------------------------')

# 리스트에 포함된 요소 갯수 세기 (count)
a= [1,2,3,4,5,3,2]
print(a.count(3))

print('-----------------------------------------')

# 리스트 확장 (extend)
# 리스트 추가
a = [1,2,3]
a.extend([4,5])
print(a)
b = [10,20]
a.extend(b)
print(a)






