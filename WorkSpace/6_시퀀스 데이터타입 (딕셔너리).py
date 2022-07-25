# 순서있는 데이터타입(인덱싱, 슬라이싱)
# - 리스트, 튜플

# 순서없는 데이터타입
# - 딕셔너리, 세트  // 인덱싱, 슬라이싱 사용 불가

# 변경가능(mutable) 데이터타입
# - 리스트, 딕셔너리, 세트

# --------------------------------------


# 딕셔너리
# 키(key) 와 값(Value) 으로 저장

dic = {1:'a',2:'b',3:'c'}
print(dic, type(dic))

dic = {'name' : '홍길동' , 'phone' : '01012345678', 'birth' : '123456'}
print(dic)

a = {1:[1,2,3]} # 값에 리스트 추가 가능
print(a)

# a= {[1,2,3]:3}  // 키(Key) 에는 리스트 사용 불가
# print(a)

# 딕셔너리에 쌍 추가하기
a = {1:'aa'}
a[2] ='bb'
print(a)
a['a'] = 'cc'
print(a)
a[3] = ['dd']
print(a)
print('---------- 다음 장--------------------')

# 딕서녀리 요소 삭제하기
del(a[3])
print(a)

print('--------- 다음장 -------------------')

# 키(Key) 를 사용해서 값(Value) 얻기
# 딕셔너리 에서 a[2] 의 의미는 리스트나 튜플과는 다르다
print(a[2])

# 딕셔너리를 만들때 중복되는 경우
a = {1:'a', 1:'b'} # 키는 중복이 불가함 (덮어 씌어져서 출력됨)
print(a)

# Key에 리스트는 사용할수없음 , 그러나 튜플은 사용가능
# key에는 변하지않는 값을 사용해야함
a = {(1,2):'a'}
print(a)

# 딕셔너리 관련 함수들

# Key , Value 리스트 만들기
a = {'name' : '홍길동' , 'phone' : '01012345678', 'birth' : '123456'}
print(dic.keys()) # Key 값이 리스트 로 출력
print(dic.values()) # Value 값이 리스트 로 출력
print(dic.items()) # 전체 가 리스트로 묶임


# 예습: 시퀀스 활용해서 반복문 만들기
for k in dic.keys():
    print(k)
print("---------------------------")

for k in dic.values():
    print(k)
print('------------------------')

for k,v in dic.items():
    print(k,v)


print('-----------------')

# # 요소 모두 지우기(clear)
# a = {'name' : '홍길동' , 'phone' : '01012345678', 'birth' : '123456'}
# dic.clear()
# print(dic)

# Key 로 Value 얻기 (get)
print(dic.get('phone'))
print(dic.get('birth'))
print(dic.get('name'))
print(dic.get('phone1')) # Key 값이 없을경우 None 리턴 ,'거짓'
print(dic.get('phone2', -1)) #  phone 이라는 Key 가 없을경우 디폴트값 리턴


# 해당 Key 가 딕셔너리 안에 있는지 조사 (in)
print('phone' in dic) # 딕셔너리 안에 존재 하니 참
print('phone1' in dic) # 딕셔너리 안에 존재 하지않으니 거짓


# 표현
# 리스트 :[]
# 튜플 : ()
# 딕셔너리 : {}






