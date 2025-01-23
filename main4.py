#숫자로 입력값 숫자를 받아서 가운데가 비어있는 이등변삼각형을 출력하세요.
#숫자가 1일 경우에는 O 하나만 출력하세요.
# 삼각형을 마지막 좌측에 맞게 그리기 가장 마지막 열에 왼쪽 끝에 닿도록
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

# 입력값 받기
strA = input('숫자를 입력하세요.')
numA = int(strA)

# 원의 시작 위치 설정
circle_x = WINDOW_WIDTH // 2  # 가운데 정렬
circle_y = 30  # 시작 높이

# 입력값만큼 원 그리기
if numA == 1:
    pygame.draw.circle(display_surface, RED, (circle_x, circle_y), 5, 0)  # 숫자 1일 경우 빨간색 원 출력
else:
    start_x = 5 # 왼쪽 끝에서 시작
    # 첫 번째 줄 (맨 위)
    pygame.draw.circle(display_surface, RED, (start_x + (numA - 1) * 30, circle_y), 5, 0)

    # 중간 줄
    for i in range(1, numA - 1):
        circle_y += 30  # 줄 간격
        # 양쪽 끝에만 원 그리기, start_x 기준으로 x 좌표 계산
        pygame.draw.circle(display_surface, GREEN, (start_x + (numA - 1 - i) * 30, circle_y), 5, 0)  
        pygame.draw.circle(display_surface, BLACK, (start_x + (numA - 1 + i) * 30, circle_y), 5, 0)  

    # 마지막 줄 (맨 아래, 삼각형 모양, 왼쪽 끝에 닿도록 조정)
    circle_y += 30
    for i in range(numA * 2 - 1):  # 밑변에 원 출력
        pygame.draw.circle(display_surface, WHITE, (start_x + i * 30, circle_y), 5, 0)
        

# 게임이 동작하는 동안 이벤트
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 디스플레이 업데이트
    pygame.display.update()

# pygame 종료
pygame.quit()

