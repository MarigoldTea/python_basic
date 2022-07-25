# 패키지 (Package)
# 모듈을 디렉토리 구조로 관리할수 있게 해준다

# 파이썬에서 모듈은 하나의 .py 파일이다



# Ex)
# Game

#   Graphics
#          screen
#          render
#   Soundtrack
#         mp3
#         wav
#   play
#      walk
#      run
#


import Game.Soundtrack.mp3.play as Soundtrack
# from Game.sound.mp3.play import play1

Soundtrack.play1()