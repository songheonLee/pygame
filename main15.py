#1일 경우, 한개의 원이 두 점 (0,200), (300,200)을 무한 왕복하게 하고(원 1개 출력)
#2일 경우, 1일 경우를 실행하면서 또 다른 한개의 원이 (0,300), (300,300)을 무한 왕복하게 하고(원 2개 출력)
#3일 경우, 2일 경우를 실행하면서 또 다른 한개의 원이 (0,400), (300,400)을 무한 왕복하게 하고(원 3개 출력)
#……
#5일 경우, 4일 경우를 실행하면서 또 다른 한개의 원이 (0,600), (300,600)을 무한 왕복하게 함.(원 5개 출력)
#단 애니메이션을 아래와 같이 반복해야 함
#1~30 프레임에는 반지름이 30인 원을 출력하고, 31 ~ 60 프레임에는 가로 반지름 27, 세로 반지름 34짜리 타원을 출력하고 그 다음 프레임은 위의 프레임을 반복 
import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
width, height = 800, 700
display_surface = pygame.display.set_mode((width, height))
# 창 제목 설정
pygame.display.set_caption("원 애니메이션")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


# 표시할 원의 개수 (초기값: 1)
num_circles = 1

# FPS 설정
fps = 60
clock = pygame.time.Clock()

# 원 데이터를 저장할 리스트 생성(위치, 목표 지점)
circle_data = []

frame = 0  # 프레임 카운터 변수 추가

# 새로운 원을 생성하는 함수
def create_circle(offset_y):
    # 원의 초기 x 좌표
    circle_x = 0
    # 원의 초기 y 좌표 (offset_y 값으로 높이 조절)
    circle_y = 200 + offset_y
    # 현재 목표 지점 인덱스 (초기값: 0)
    current_target = 0
    # 원이 움직일 목표 지점 좌표 리스트
    targets = [(0, circle_y), (300, circle_y)]
    # 원 데이터를 circle_data 리스트에 추가
    circle_data.append([circle_x, circle_y, current_target, targets])

# 초기 원 생성
create_circle(0)

# 게임 루프 시작
running = True 

while running: #무한 루프
    
    frame += 1  # 프레임 카운터 증가
    if frame > 60:  # 60 프레임마다 초기화
        frame = 1
    
    # 이벤트 처리
    for event in pygame.event.get():
        # 창 닫기 이벤트 처리
        if event.type == pygame.QUIT:
            running = False
        # 키 입력 이벤트 처리
        if event.type == pygame.KEYDOWN:
            # 숫자 키 (1~5) 입력 처리
            if event.key in range(pygame.K_1, pygame.K_6):
                # num_circles 값 업데이트
                num_circles = event.key - pygame.K_0
                # 기존 원 데이터 삭제
                circle_data.clear()
                # 새로운 원 생성
                for i in range(num_circles):
                    create_circle(i * 100)
                
    
    # 원 위치 업데이트
    for i in range(len(circle_data)):
        # 현재 원 데이터 가져오기
        x, y, current_target, targets = circle_data[i]
        # 현재 목표 지점 좌표 가져오기
        target_x, target_y = targets[current_target]

        # x, y 이동 거리 계산
        ax = target_x - x
        ay = target_y - y
        # 현재 위치와 목표 지점 사이의 거리 계산
        distance = (ax**2 + ay**2)**0.5

        # 목표 지점에 도달하지 않았으면 이동
        if distance > 1:
            x += ax / distance
            y += ay / distance
        # 목표 지점에 도달했으면 다음 목표 지점으로 변경
        else:
            current_target = (current_target + 1) % len(targets)

        # 업데이트된 원 데이터 저장
        circle_data[i] = [x, y, current_target, targets]

    
    # 화면을 흰색으로 채우기
    display_surface.fill(white)
    # 모든 원 그리기
    for x, y, _, _ in circle_data: # 각 원의 x, y 좌표를 가져옴 current_target, targets 값 무시 
        if frame <= 30:
            pygame.draw.circle(display_surface, red, (int(x), int(y)), 30)  # 원 그리기  x값, y값, 반지름
        else:
            pygame.draw.ellipse(display_surface, red, (int(x) - 27, int(y) - 34, 54, 68))  # 타원 그리기 x값, y값, 가로, 세로
    # 화면 업데이트
    pygame.display.update()

    # 프레임 속도 유지
    clock.tick(fps)

# Pygame 종료
pygame.quit()