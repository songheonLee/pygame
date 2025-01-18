import pygame

# pygame 초기화
pygame.init()

# 창 크기 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# RGE 색상 기준으로 사용할 색깔 정의
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

#input으로 입력값 받기
strA = int(input('숫자를 입력하세요.'))

#원의 간격 설정
circle_spacing = 1

#원의 시작 위치 설정
circle_x = 0
circle_y = 0

# 입력값 만큼 원 그리기
for i in range(strA):
    pygame.draw.circle(display_surface, WHITE, (circle_x, circle_y), 2, 0)

    

    #다음 원 그릴 위치
    circle_x += circle_spacing
    circle_y += circle_spacing


#게임이 동작하는 동안 이벤트
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #디스플레이 업데이트
    pygame.display.update()

# pygame 종료
pygame.quit()

