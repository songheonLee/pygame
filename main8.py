#키보드 입력을 통해서 다양한 도형 출력 하기
#키보드를 통해서 도형의 종류(L : line, C: circle, R: Rect, T: Triangle, D: Diamond)를 입력 받고 
	#만일 선일 경우에는 cmd를 통해서 시작점과 끝점과 선분의 굵기와 색상을 입력받아서 출력
	#만일 원일 경우에는 cmd를 통해서 중점과 반지름과 선분의 굵기와 색상을 입력받아서 출력
	#만일 네모일 경우에는 cmd를 통해서 왼쪽 상단점과 오른쪽 하단점, 선분의 굵기와 색상을 입력받아서 출력
	#만일 삼각형일 경우에는 cmd를 통해서 삼각형의 높이를 입력받아서 화면에 출력
	#만일 다이아몬드일 경우에는 cmd를 통해서 다이아몬드의 높이를 입력받아서 화면에 출력


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



# 게임이 동작하는 동안 이벤트 처리 
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        if event.type == pygame.KEYDOWN:
            # 백그라운드 색깔 설정
            display_surface.fill(BLUE)
            # 선 그리기 (L 키)
            if event.key == pygame.K_l:
                start_x = int(input("시작점 x 좌표를 입력하세요: "))
                start_y = int(input("시작점 y 좌표를 입력하세요: "))
                end_x = int(input("끝점 x 좌표를 입력하세요: "))
                end_y = int(input("끝점 y 좌표를 입력하세요: "))
                thickness = int(input("선분의 굵기를 입력하세요: "))
                color_str = input("선분의 색상을 입력하세요 (RED, GREEN, BLUE, WHITE, BLACK): ").upper()
                color = {
                    'RED': RED,
                    'GREEN': GREEN,
                    'BLUE': BLUE,
                    'WHITE': WHITE,
                    'BLACK': BLACK
                }[color_str]
                pygame.draw.line(display_surface, color, (start_x, start_y), (end_x, end_y), thickness)

            # 원 그리기 (C 키)
            elif event.key == pygame.K_c:
                center_x = int(input("원의 중심 x 좌표를 입력하세요: "))
                center_y = int(input("원의 중심 y 좌표를 입력하세요: "))
                radius = int(input("원의 반지름을 입력하세요: "))
                thickness = int(input("선분의 굵기를 입력하세요: "))
                color_str = input("원의 색상을 입력하세요 (RED, GREEN, BLUE, WHITE, BLACK): ").upper()
                color = {
                    'RED': RED,
                    'GREEN': GREEN,
                    'BLUE': BLUE,
                    'WHITE': WHITE,
                    'BLACK': BLACK
                }[color_str]
                pygame.draw.circle(display_surface, color, (center_x, center_y), radius, thickness)
                

            # 네모 그리기 (R 키)
            elif event.key == pygame.K_r:
                left_x = int(input("왼쪽 상단점 x 좌표를 입력하세요: "))
                left_y = int(input("왼쪽 상단점 y 좌표를 입력하세요: "))
                right_x = int(input("오른쪽 하단점 x 좌표를 입력하세요: "))
                right_y = int(input("오른쪽 하단점 y 좌표를 입력하세요: "))
                color_str = input("네모의 색상을 입력하세요 (RED, GREEN, BLUE, WHITE, BLACK): ").upper()
                color = {
                    'RED': RED,
                    'GREEN': GREEN,
                    'BLUE': BLUE,
                    'WHITE': WHITE,
                    'BLACK': BLACK
                }[color_str]
                pygame.draw.rect(display_surface, color, pygame.Rect(left_x, left_y, right_x - left_x, right_y - left_y))
                
            # 삼각형 그리기 (T 키)
            elif event.key == pygame.K_t:
                height = int(input("삼각형의 높이를 입력하세요: "))
                center_x = WINDOW_WIDTH // 2 # 화면의 폭 나누기 2의 몫
                center_y = WINDOW_HEIGHT // 2 # 화면의 높이 나누기 2의 몫
                points = [
                    (center_x, center_y - height // 2), # 첫 번쨰 꼭짓점 =중심점에서 위쪽으로 높이의 절반만큼 이동한 위치
                    (center_x - height // 2, center_y + height // 2), # 두 번쨰 꼭짓점= 중심점에서 왼쪽 아래로 높이의 절반만큼 이동한 위치
                    (center_x + height // 2, center_y + height // 2) # 세 번쨰 꼭짓점 = 중심점에서 오른쪽 아래로 높이의 절반만큼 이동한 위치
                ]
                color_str = input("삼각형의 색상을 입력하세요 (RED, GREEN, BLUE, WHITE, BLACK): ").upper()
                color = {
                    'RED': RED,
                    'GREEN': GREEN,
                    'BLUE': BLUE,
                    'WHITE': WHITE,
                    'BLACK': BLACK
                }[color_str]
                pygame.draw.polygon(display_surface, color, points)  # 삼각형 그리기
                
            # 다이아몬드 그리기 (D 키)
            elif event.key == pygame.K_d:
                height = int(input("다이아몬드의 높이를 입력하세요: "))
                # 다이아몬드의 꼭짓점 계산
                center_x = WINDOW_WIDTH // 2 # 화면의 폭 나누기 2의 몫
                center_y = WINDOW_HEIGHT // 2 # 화면의 높이 나누기 2의 몫
                points = [
                    (center_x, center_y - height // 2), # 첫 번쨰 꼭짓점 = 중심점에서 위쪽으로 높이의 절반만큼 이동한 위치
                    (center_x - height // 2, center_y), # 두 번쨰 꼭짓점 = 중심점에서 왼쪽으로 높이의 절반만큼 이동한 위치
                    (center_x, center_y + height // 2), # 세 번쨰 꼭짓점 = 중심점에서 아래쪽으로 높이의 절반만큼 이동한 위치
                    (center_x + height // 2, center_y)  # 네번 번쨰 꼭짓점 = 중심점에서 오른쪽으로 높이의 절반만큼 이동한 위치
                ]
                color_str = input("다이아몬드의 색상을 입력하세요 (RED, GREEN, BLUE, WHITE, BLACK): ").upper()
                color = {
                    'RED': RED,
                    'GREEN': GREEN,
                    'BLUE': BLUE,
                    'WHITE': WHITE,
                    'BLACK': BLACK
                }[color_str]
                pygame.draw.polygon(display_surface, color, points)  # 다이아몬드 그리기
                
        pygame.display.update()
        
pygame.quit()
