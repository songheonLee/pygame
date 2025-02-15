#반지름이 10인 원을 (0, 0)에 출력하고 
#FPS가 60을 고정된 상태에서
#l를 누르면 두 점 (0,200), (300,200)을 무한 왕복하게 하고
#t를 누르면 세 점 (150, 0), (0,200), (300,200)을 무한으로 왕복(A -> B -> C -> A -> B ......)하게 하고
#option
#c를 누르면 중심이(150, 150)이고 반지름이 100인 원을 무한대로 반시계 방향으로 빙글빙글 돌도록 함
import pygame

pygame.init()

# 화면 설정
width, height = 600, 400
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("원 애니메이션")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 원 설정
circle_x, circle_y = 0, 0  # 초기 위치
circle_radius = 10

# FPS 설정
clock = pygame.time.Clock()
fps = 60

# 애니메이션 모드
animation_mode = None  # none, line, triangle, circle

# 애니메이션 타겟
line_targets = [(0, 200), (300, 200)]
triangle_targets = [(150, 0), (0, 200), (300, 200)]
current_target_index = 0

# 원 회전 설정
circle2_x, circle2_y = 150, 150  # 회전 중심
circle2_radius = 100
circle2_angle = 0  # 초기 각도
circle2_speed = 5  # 회전 속도

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                animation_mode = "line"
                current_target_index = 0
            elif event.key == pygame.K_t:
                animation_mode = "triangle"
                current_target_index = 0
            elif event.key == pygame.K_c:
                animation_mode = "circle"

    # 화면 지우기
    display_surface.fill(white)

    # 애니메이션 로직
    if animation_mode:
        if animation_mode == "line" or animation_mode == "triangle":
            targets = line_targets if animation_mode == "line" else triangle_targets
            target_x, target_y = targets[current_target_index]

            # 원 이동
            dx = target_x - circle_x
            dy = target_y - circle_y
            distance = (dx**2 + dy**2)**0.5

            if distance > 1:
                circle_x += dx / distance
                circle_y += dy / distance
            else:
                current_target_index = (current_target_index + 1) % len(targets)

             # 원 그리기
            pygame.draw.circle(display_surface, red, (int(circle_x), int(circle_y)), circle_radius)

        elif animation_mode == "circle":
            # 원 회전



 



