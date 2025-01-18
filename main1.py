import pygame

#pygame초기화
pygame.init()

#창 크기 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

#RGE 색상 기준으로 사용할 색깔 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#창 설정
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello World!')

#백그라운드 색깔 설정
display_surface.fill(BLUE)

#line 함수를 이용해 라인 그리기 
pygame.draw.line(display_surface, RED, (100,100), (200,200), 3)

#circule() 함수를 이용해 하얀색으로 동그라미 그리기
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 50, 3)

#Rectangle()함수를 이용해 녹색을 네모칸 그리기
pygame.draw.rect(display_surface, GREEN, (300, 0, 100, 100),3)

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