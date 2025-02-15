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

# 원의 초기 위치 설정
circle_radius = 10

# 창 설정
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('q로 애니메이션 수행')

# 애니메이션 변수
is_moving = False # 애니메이션 중인지 여부
start_x = 0
end_x = 200
y = 150

# 현재 원의 위치
current_x = start_x

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # 키 입력 처리 
    keys = pygame.key.get_pressed()

    # q 키를 눌렀을 떄 (애니메이션 시작)
    if keys[pygame.K_q] and not is_moving:
        is_moving = True
    
    # 원이 애니메이션을 통해 이동 중일 떄
    if is_moving:
        if current_x < end_x:
            current_x += 1
        else:
            is_moving = False # 애니메이션 끝

    # 화면을 흰색으로 채우기
    display_surface.fill(WHITE)

    # 원 그리기
    pygame.draw.circle(display_surface, RED, (current_x, y), circle_radius)

    # 화면 업데이트
    pygame.display.update()

    # FPS 설정
    clock.tick(60)


