import pygame

pygame.init() #초기화 과정으로 반드시 해줘야 함

# 화면 크기 설정
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

# 타이틀 화면 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\wjdtj\\Desktop\\Python Workspace\\pygame_basic\\background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기
    pygame.display.update() # 화면 계속 새로고침

# pygame 종료
pygame.quit()