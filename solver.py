import pygame

pygame.init()

board1 = []
board2 = []
rubic =  []

def initBoard(boardType):
	global width, board1, board2
	if boardType == 1:
		x = 240
		y = 780
		for i in range(5):
			for j in range(5):
				board1.append((x, y, 60, 60))
				x = x + 60
			y = y + 60
			x = 240
	elif boardType == 2:
		x = 240
		y = 0
		for i in range(5):
			for j in range(5):
				board1.append((x, y, 60, 60))
				x = x + 60
			y = y - 60
			x = 240

initBoard(1)
initBoard(2)

def drawGrid(width, rows, surface):
	global board1, board2, rubic
	sizeBtwn = width // rows

	x = 0
	y = 0
	i = 0
	j = 0

	pygame.draw.line(surface, (255, 255, 255), (240, 0), (540, 0))
	pygame.draw.line(surface, (255, 255, 255), (240, width-1), (540, width-1))
	for i in range(len(board1)):
		pygame.draw.rect(surface, (0, 0, 255), (board1[i]))
	for i in range(len(board2)):
		pygame.draw.rect(surface, (0, 0, 255), (board2[i]))
	i = 0
	for l in range(rows):
		x = x + sizeBtwn
		y = y + sizeBtwn
		if i > 2 and i < 9:
			pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, 300))
			pygame.draw.line(surface, (255, 255, 255), (x, width), (x, 480))
			if i > 3 and i < 8:
				pygame.draw.line(surface, (255, 255, 255), (x, 300), (x, 480))
		if j != 5 and j != 6:
			pygame.draw.line(surface, (255, 255, 255), (240, y), (540, y))
		else:
			pygame.draw.line(surface, (255, 255, 255), (300, y), (480, y))
		i = i + 1
		j = j + 1

flag = True

clock = pygame.time.Clock()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

height = 780
width = 780
rows = 13

size = (height, width)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

while flag:
	pygame.time.delay(5)
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			flag = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				print("Player moved up!")
			elif event.key == pygame.K_a:
				print("Player moved left!")
			elif event.key == pygame.K_s:
				print("Player moved down!")
			elif event.key == pygame.K_d:
				print("Player moved right!")
	drawGrid(width, rows, screen)
	pygame.display.update()
pygame.quit()
