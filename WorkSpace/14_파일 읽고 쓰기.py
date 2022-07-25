 # 파일객체 = open(파일명, 모드 , 인코딩)
 #
 # 파일 객체 멤버함수
 # write
 # read
 # readline
 # readlines
 # seek
 # tell
 # close

# 파일열기모드
# r - 읽기모드
# w - 쓰기모드
# a - 추가모드


# fp = open("test.txt", "w")
#
# for i in range(1, 11):
#     fp.write(f"{i} 입니다\n")
#
# fp.close()

# 파일 읽기
# fp = open("test.txt", 'r')
# rd = fp.read()
# fp.close()
#
# print(rd)

# 원하는 글자 수 만 불러온다
# fp = open("test.txt", 'r')
# rd = fp.read(10)
# fp.close()
#
# print(rd)


# 파일 포인터 위치 (tell)
# fp = open("test2.txt", "w")
# print(fp.tell())
# fp.write("asdadasdasdad")
# print(fp.tell())
# fp.write("Hello World")
# fp.close()

# 파일 포인터 변경 (seek)
# fp = open("test2.txt", "w")
# print(fp.tell()) # 포인터 0
# fp.write("asdadasdasdad")
# fp.seek(3)
# print(fp.tell())
# fp.write("Hello World")
# fp.close()


# 파일 읽기(readline)
# fp = open("test.txt", "r")
# line = fp.readline()
# print(line)
# fp.close()

# fp = open("test.txt", "r")
# for i in fp:
#     print(i)
# fp.close()


#  파일 읽기 (readlines) # list 로 출력
# fp = open("test.txt", "r")
# rd = fp.readlines()
# for i in rd:
#     i = i.strip()
# print(i)
# fp.close()

# 추가 모드
# fp = open("test.txt", 'a')
# for i in range(11, 21):
#     fp.write(f"{i} 입니다\n")
# fp.close()

# 응용
# def fileWrite(file, args, mode = "w"):
#     fp = open(f"{file}.txt", mode)
#     for i in args:
#         fp.write(i)
#     fp.close()
#
#
#
# fileWrite("test", "배고픔", "a")

def fileWrite(filename, args, mode="w"):
     fp = open(f"{filename}.txt", mode)
     for i in args:
         fp.write(i)
     fp.close()


 def fileReadline(filename, line):


 # 원하는 줄수 출력


 fileWrite("test", "dsafasdfsdafsadfsda", "a")
 fileReadline("test", 3)


