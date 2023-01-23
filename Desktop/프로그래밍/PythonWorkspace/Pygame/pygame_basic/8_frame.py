import pygame

# 기본 초기화 (반드시 해야 하는 것들)
###############################################################
pygame.init() #초기화 과정으로 반드시 해줘야 함

# 화면 크기 설정
screen_width=480 # 가로 크기
screen_height=640 # 세로 크기
screen=pygame.display.set_mode((screen_width, screen_height))

# 타이틀 화면 설정
pygame.display.set_caption("내 첫 게임")

# FPS
clock = pygame.time.Clock()
###############################################################

#  1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 프레임

    print("fps: " + str(clock.get_fps()))
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임이 진행중이 아님
    
    # 3. 게임 캐릭터 위치 정의


    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update() # 화면 계속 새로고침

# 게임 종료 후에도 잠시 기다리기
pygame.time.delay(2000) # 게임 종료 후 2초 대기

# pygame 종료
pygame.quit()