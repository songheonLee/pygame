#FPS가 60을 고정된 상태에서, 반지름이 40인 원을 (60, 200)에 출력하고 
#1~30 프레임에는 반지름이 40인 원을 출력하고, 31 ~ 60 프레임에는 가로 반지름 35, 세로 반지름 45짜리 타원을 출력하고 그 다음 프레임은 위의 프레임을 반복 

import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
width, height = 600, 400
display_surface = pygame.display.set_mode((width, height))
# 창 제목 설정
pygame.display.set_caption("원 애니메이션")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 원의 반지름 설정
radius = 40

# FPS 설정
fps = 60
clock = pygame.time.Clock()

x = 60  # x값 30
y = 200  # y값 200

ax = 23
ay = 157
frame = 0  # 프레임 카운터 변수 추가

running = True

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        # 창 닫기 이벤트 처리
        if event.type == pygame.QUIT:
            running = False

    frame += 1  # 프레임 카운터 증가
    if frame > 60:  # 60 프레임마다 초기화
        frame = 1

    # 화면을 흰색으로 채우기 
    display_surface.fill(white)

    # 프레임에 따라 원 또는 타원 그리기
    if frame <= 30:
        pygame.draw.circle(display_surface, red, (x, y), radius)  # 원 그리기
    else:
        pygame.draw.ellipse(display_surface, red, (ax, ay, 70, 90))  # 타원 그리기

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정
    clock.tick(fps)

pygame.quit()  # Pygame 종료