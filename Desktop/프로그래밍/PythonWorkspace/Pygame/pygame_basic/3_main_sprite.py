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

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\wjdtj\\Desktop\\Python Workspace\\pygame_basic\\character.png")
chracter_size = character.get_rect().size # 이미지의 크기를 구해옴
chracter_width = chracter_size[0] # 캐릭터의 가로 크기
chracter_height = chracter_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - (chracter_width/2) # 화면 가로의 절반에 위치(정중앙)
character_y_pos = screen_height - chracter_height # 화면 세로 가장 아래에

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 화면에 캐릭터 표시

    pygame.display.update() # 화면 계속 새로고침

# pygame 종료
pygame.quit()