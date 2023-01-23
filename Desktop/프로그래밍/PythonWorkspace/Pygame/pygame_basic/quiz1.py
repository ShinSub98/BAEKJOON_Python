# 1. 캐릭터는 화면 가장 아래 위치, 좌우만 이동
# 2. 똥은 화면 가장 위에서 떨어짐. x좌표는 랜덤으로
# 3. 캐릭터가 똥을 피하면 다음 똥이 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. fps는 30으로 고정

# [게임 이미지]
# 1. 배경: 640*480
# 2. 캐릭터: 70*70
# 3. 똥: 35*35



from msilib.schema import Class
import pygame
from random import *

# 기본 초기화 (반드시 해야 하는 것들)
###############################################################
pygame.init() #초기화 과정으로 반드시 해줘야 함

# 화면 크기 설정
screen_width=480 # 가로 크기
screen_height=640 # 세로 크기
screen=pygame.display.set_mode((screen_width, screen_height))

# 타이틀 화면 설정
pygame.display.set_caption("신정섭의 똥피하기")

# FPS
clock = pygame.time.Clock()
###############################################################

#  1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("background.jpg")

character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

character_speed = 0.6

to_x = 0

# 적 캐릭터1
poo = pygame.image.load("poo.png")
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_x_pos = randint(0, screen_width-poo_width)
poo_y_pos = poo_height

poo_speed = 8


# 적 캐릭터2
poo2 = pygame.image.load("poo.png")
poo2_size = poo2.get_rect().size
poo2_width = poo2_size[0]
poo2_height = poo2_size[1]
poo2_x_pos = randint(0, screen_width-poo_width)
poo2_y_pos = -(screen_height/3)

# poo2_speed = 8

# 적 캐릭터3
poo3 = pygame.image.load("poo.png")
poo3_size = poo3.get_rect().size
poo3_width = poo3_size[0]
poo3_height = poo3_size[1]
poo3_x_pos = randrange(0, screen_width-poo_width)
poo3_y_pos = -((screen_height/3)*2)

# poo3_speed = 8

# # 적 캐릭터4
# poo4 = pygame.image.load("C:\\Users\\wjdtj\\Desktop\\Python Workspace\\pre_game\\poo.png")
# poo4_size = poo4.get_rect().size
# poo4_width = poo4_size[0]
# poo4_height = poo4_size[1]
# poo4_x_pos = randrange(0, screen_width-poo_width)
# poo4_y_pos = poo_height + screen_height


# 폰트 정의
game_font = pygame.font.Font(None, 40)

start_ticks = pygame.time.get_ticks()

# 피한 똥
count = 0

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 프레임

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임이 진행중이 아님 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
        
        # 똥이 떨어지면
    if poo_y_pos > screen_height:
            poo_y_pos = 0
            poo_x_pos = randint(0, screen_width-poo_width)
            count += 1
        
    if poo2_y_pos > screen_height:
            poo2_y_pos = 0
            poo2_x_pos = randint(0, screen_width-poo_width)
            count += 1

    if poo3_y_pos > screen_height:
            poo3_y_pos = 0
            poo3_x_pos = randint(0, screen_width-poo_width)
            count += 1

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    poo_y_pos += poo_speed
    poo2_y_pos += poo_speed
    poo3_y_pos += poo_speed

    # 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poo_rect = poo.get_rect()
    poo_rect.left = poo_x_pos
    poo_rect.top = poo_y_pos

    poo2_rect = poo2.get_rect()
    poo2_rect.left = poo2_x_pos
    poo2_rect.top = poo2_y_pos

    poo3_rect = poo3.get_rect()
    poo3_rect.left = poo3_x_pos
    poo3_rect.top = poo3_y_pos

    # 충돌 체크
    if character_rect.colliderect(poo_rect) or character_rect.colliderect(poo2_rect) or character_rect.colliderect(poo3_rect):
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poo, (poo_x_pos, poo_y_pos))
    screen.blit(poo2, (poo2_x_pos, poo2_y_pos))
    screen.blit(poo3, (poo3_x_pos, poo3_y_pos))

    # 타이머 생성
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000

    timer = game_font.render("Play Time: "+str(int(elapsed_time))+"s", True, (0,0,0))
    screen.blit(timer, (10, 10))

    score = game_font.render("Score: "+str(count), True, (0,0,0))
    screen.blit(score, (10, 40))

    if count == 15:
        poo_speed += 0.2
    if count == 25:
        poo_speed += 0.2
    if count == 35:
        poo_speed += 0.2


    pygame.display.update() # 화면 계속 새로고침

board1 = game_font.render("Oops!",True, (0,0,0))
board2 = game_font.render("Time: "+str(int(elapsed_time))+" sec", True, (0,0,0))
board3 = game_font.render("Score: "+str(count)+" points", True, (0,0,0))
screen.blit(board1,(200,200))
screen.blit(board2,(165,230))
screen.blit(board3,(130,260))

pygame.display.update()
print("으악!")
print("버틴 시간:",str(int(elapsed_time)),"초")
print("피한 똥:",count,"개")
pygame.time.delay(2000) # 게임 종료 후에도 잠시 기다리기

# pygame 종료
pygame.quit()