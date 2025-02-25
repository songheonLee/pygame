#반지름이 10인 원을 (0, 0)에 출력하고 
#FPS가 60을 고정된 상태에서
#l를 누르면 두 점 (0,200), (300,200)을 무한 왕복하게 하고
#t를 누르면 세 점 (150, 0), (0,200), (300,200)을 무한으로 왕복(A -> B -> C -> A -> B ......)하게 하고
#option
#c를 누르면 중심이(150, 150)이고 반지름이 100인 원을 무한대로 반시계 방향으로 빙글빙글 돌도록 함
import pygame

# 파이게임 초기화
pygame.init()

# 창 크기 설정
width, height = 600, 400
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("원 애니메이션")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 원 속성
radius = 10
x, y = 0, 0  # 초기 위치

# 애니메이션 변수
fps = 60 # 초당 프레임 수 60 설정
clock = pygame.time.Clock() # 프레임 속도를 제어
animation_mode = None  # 애니메이션 모드 처음은 none으로 저장
current_target = 0  # 현재 목표 지점 인덱스 애니메이션의 시작점을 설정

# 각 애니메이션 모드의 목표 지점
line_targets = [(0, 200), (300, 200)] # 직선 좌표
triangle_targets = [(150, 0), (0, 200), (300, 200)] # 삼각형 좌표

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 창 닫기 버튼을 누르면 종료
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                animation_mode = "line"  # 'L' 키를 누르면 직선 애니메이션 시작
                x, y = line_targets[0]
                current_target = 0 # 인덱스의 초기 값을 0 애니메이션이 시작될 때 원은 첫 번째 목표 지점으로 이동
            elif event.key == pygame.K_t:
                animation_mode = "triangle"  # 't' 키를 누르면 삼각형 애니메이션 시작
                current_target = 0
                x, y = triangle_targets[current_target]
                

    # 애니메이션 로직
    if animation_mode:
        # 현재 애니메이션 모드에 따라 목표 지점 설정
        target_x, target_y = (line_targets if animation_mode == "line" else triangle_targets)[current_target] #[current_target]은 변수 값을 인덱스로 사용하여 특정 요소를 선택
        
        # 목표 지점으로 이동``
        
        ax = target_x - x # 원의 현재 x 좌표와 목표 지점의 x 좌표 사이의 거리를 계산해 ax 에 저장
        ay = target_y - y
        distance = (ax**2 + ay**2)**0.5
        # distance = 원의 현재 위치와 목표 위치 사이의 전체 거리 피타고라스 정리를 사용하여 원의 현재 위치와 목표 지점 사이의 거리를 계산 ()의 0.5제곱은 √() 제곱근을 구하는 것
       
        if distance > 0.1:  # 목표 지점에 도착하지 않았으면 원을 이동 거리가 1보다 크면 아직 목표 지점에 도착하지 않은 것으로 간주
            
            x += ax / distance #ax = 원이 이동해야 할 x축 방향의 거리, 원을 x축 방향으로 이동시키는 코드 원이 이동해야 할 x축 방향의 거리 (ax) 를 전체 거리 (distance) 로 나눈 값
            y += ay / distance
        else:
            # # (current_target + 1)을 목표 지점 목록의 길이로 나눈 나머지를 계산 코드
            current_target = (current_target + 1) % len((line_targets if animation_mode == "line" else triangle_targets)) 
            # 1 증가시켜 다음 목표 지점으로 전환합니다. 
            # % 연산자는 인덱스가 목표 지점 목록의 범위를 벗어나지 않도록 합니다 (즉, 목록의 마지막 요소에 도달하면 다시 첫 번째 요소로 돌아갑니다). 
            # len(): 목표 지점 목록의 길이를 계산 
            print(current_target)
    # 화면을 흰색으로 채우기
    display_surface.fill(white)

    # 원 그리기
    pygame.draw.circle(display_surface, red, (int(x), int(y)), radius)

    # 화면 업데이트
    pygame.display.update()

    # FPS 설정
    clock.tick(fps)

pygame.quit()  # 파이게임 종료