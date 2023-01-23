import pygame
import os

# 기본 초기화 (반드시 해야 하는 것들)
###############################################################
pygame.init() #초기화 과정으로 반드시 해줘야 함

# 화면 크기 설정
screen_width=640 # 가로 크기
screen_height=480 # 세로 크기
screen=pygame.display.set_mode((screen_width, screen_height))

# 타이틀 화면 설정
pygame.display.set_caption("신정섭의 팡")

# FPS
clock = pygame.time.Clock()
###############################################################

#  1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)  # __file__ = 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이 위에 캐릭터를 올려두기 위해

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2 - character_width/2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 개 발사 가능
weapons = []

# 무기 속도
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18,-15,-12,-9] #index 0,1,2,3에 해당하는 값

# 공들
balls = []

# 최초로 발생하는 큰 공 추가
balls.append({
    "pos_x":50, #공의 x좌표
    "pos_y":50,  #공의 y좌표
    "img_idx":0, #공의 이미지 인덱스
    "to_x":3, #x축 이동 방향 (양수면 오른쪽, 음수면 왼쪽)
    "to_y": -6, #y축 이동방향
    "init_spd_y": ball_speed_y[0]})#y 최초 속도


running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 프레임

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_to_x > screen_width-character_width:
        character_x_pos = screen_width-character_width
    
    # 무기 위치 조정
    # 100, 200 -> 
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 발사

    # 천장에 닿은 무기 지우기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0] # 무기는 y좌표가 0보다 클 때만 존재한다는 조건 생성

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"] # ball_pos_x에 pos_x를 삽입
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공의 이동 방향 변경 (튕기는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"]*-1
        
        # 세로 위치
        # 스테이지에 튕겨 올라가는 처리
        if ball_pos_y >= screen_height-stage_height-ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 스테이지에 닿지 않을 때는 포물선 형성
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
    
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))



    pygame.display.update() # 화면 계속 새로고침

# # 게임 종료 후에도 잠시 기다리기
# # 게임 종료 후 2초 대기
# pygame.time.delay(2000) 

# pygame 종료
pygame.quit()