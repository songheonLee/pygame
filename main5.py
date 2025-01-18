# cmd 창을 통해서 원의 중심과 반지름, 색상을 각각 입력받아서 출력

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

# 백그라운드 색깔 설정
display_surface.fill(BLUE)

# cmd 창을 통해 원의 정보 입력
center_x = input("원의 중심 x 좌표를 입력하세요: ")
center_y = input("원의 중심 y 좌표를 입력하세요: ")
radius = input("원의 반지름을 입력하세요: ")
color_str = input("원의 색상을 입력하세요 (RED, GREEN, BLUE, WHITE, BLACK): ").upper()

# 입력값을 정수로 처리
center_x = int(center_x)
center_y = int(center_y)
radius = int(radius)

#입력받은 색상을 RGB값으로 처리
color = {
    'RED' : RED,
    'GREEN' : GREEN,
    'BLUE' : BLUE,
    'WHITE' : WHITE,
    'BLACK' : BLACK
}[color_str]

# 원 그리기
pygame.draw.circle(display_surface, color, (center_x, center_y), radius, 0)

# 게임이 동작하는 동안 이벤트 처리
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 디스플레이 업데이트
    pygame.display.update()

# pygame 종료
pygame.quit()