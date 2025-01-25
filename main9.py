#키보드 입력을 통해서 도형 이동 하기
#최초에 200, 200위치에 반지름 100짜리 원을 그려놓고
#키보드를 통해서 방향(AWSD)를 입력 받고 
	#A 입력시 좌, W 입력시 상, S 입력시 우, D 입력시 하로 3px이동
import pygame

# pygame 초기화
pygame.init()

# 창 크기 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# RGB 색상 기준으로 사용할 색깔 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 창 설정
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello World!')

# 초기 원 위치 및 반지름
center_x = 200
center_y = 200
radius = 100
color = RED

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            display_surface.fill(BLUE) # 백그라운드 색깔
            # 키 입력에 따른 원 이동
            if event.key == pygame.K_a:  # 좌
                center_x -= 3
            elif event.key == pygame.K_d:  # 우
                center_x += 3
            elif event.key == pygame.K_w:  # 상
                center_y -= 3
            elif event.key == pygame.K_s:  # 하
                center_y += 3
            
        pygame.draw.circle(display_surface, color, (center_x, center_y), radius) # 원 그리기
        # 화면 업데이트
    pygame.display.update()

# pygame 종료
pygame.quit()