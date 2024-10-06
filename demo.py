import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Đặt kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Đơn Giản')

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)

# Vòng lặp game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Làm mới màn hình
    screen.fill(black)

    # Vẽ hình chữ nhật trắng
    pygame.draw.rect(screen, white, (width // 2 - 50, height // 2 - 50, 100, 100))

    # Cập nhật màn hình
    pygame.display.flip()
