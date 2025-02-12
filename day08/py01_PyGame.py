# py01_PyGame.py 
# pygmae 템플릿 이게 기본틀이라  22번 줄부터 작성하면 됨
import pygame # pygame 기본모듈 추가
from pygame.locals import QUIT # 종료처리변수
import sys # 운영체제 시스템 명령

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((640, 400)) ## tkinter == root.geometry('600x400')
FRSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic')

def main():
    while True:
        Surface.fill(color='azure')
        # Surface.fill((255, 255, 255)) # 백그라운드 색상 #FFFFFF = white. #'00'000000 / #'00'FFFFFF  앞에 두개의 값은 alpha 투명도,   surface는 화면을 fill은 채우다
        for event in pygame.event.get() : # 키보드 , 마우스 이벤트 체크
            if event.type == QUIT: # WM_DELETE_WINDOW
                pygame.quit()  # Pygame 종료
                sys.exit()   # 윈도우앱 종료 

        pygame.display.update() # 지금까지 작성한 코드를 윈도우 창에 표시(필수)
        FRSCLOCK.tick(30) # 30 fps 지정

if __name__=='__main__':
    main()
