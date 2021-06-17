# Counter Clockwise
# Justin D
# 10/28/2020
# Filename: Counter_Clockwise.py

try:

	import pygame
	import time
	import math

	pygame.init()

	screen = pygame.display.set_mode((500, 600))

	GREY = (150, 150, 150)  # rgb color picker on google. 0-255
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)

	running = True

	# Set up text
	font = pygame.font.SysFont('sans', 50)  # font and size
	text_1 = font.render('+', True, BLACK)  # True is for smooth and nice writing
	text_2 = font.render('-', True, BLACK)
	text_3 = font.render('+', True, BLACK)
	text_4 = font.render('-', True, BLACK)
	text_5 = font.render('Start', True, BLACK)
	text_6 = font.render('Reset', True, BLACK)

	total_secs = 0
	total = 0
	start = False
	radius_secs = 90
	radius_mins = 40

	sound = pygame.mixer.Sound('tolling-bell_daniel-simion.wav')

	clock = pygame.time.Clock()

	while running:

		clock.tick(60)

		screen.fill(GREY)  # set the color for screen

		mouse_x, mouse_y = pygame.mouse.get_pos()
		# print(mouse_x)

		pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))  # numbers stands for position (the first 2 numbers), width and length of rect in screen
		pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
		pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
		pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
		pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
		pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))

		# Show text
		screen.blit(text_1, (100, 50))
		screen.blit(text_2, (100, 200))
		screen.blit(text_3, (200, 50))
		screen.blit(text_4, (200, 200))
		screen.blit(text_5, (300, 50))
		screen.blit(text_6, (300, 150))

		pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
		pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))

		pygame.draw.circle(screen, BLACK, (250, 400), 100)
		pygame.draw.circle(screen, WHITE, (250, 400), 90)
		pygame.draw.circle(screen, BLACK, (250, 400), 5)

		#pygame.draw.line(screen, BLACK, (250, 400), (250, 310))

		for event in pygame.event.get():  # event: click mouse or touch keyboard
			if event.type == pygame.QUIT:  # QUIT button
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:  # click mouse button
				if event.button == 1:  # left click
					pygame.mixer.pause()
					if (100 < mouse_x < 150) and (50 < mouse_y < 100):
						total_secs += 60
						total = total_secs
						print("press + minute")
					if (100 < mouse_x < 150) and (200 < mouse_y < 250):
						total_secs -= 60
						total = total_secs
						print("press - minute")
					if (200 < mouse_x < 250) and (50 < mouse_y < 100):
						total_secs += 1
						total = total_secs
						print("press + minute")
					if (200 < mouse_x < 250) and (200 < mouse_y < 250):
						total_secs -= 1
						total = total_secs
						print("press - minute")
					if (300 < mouse_x < 450) and (50 < mouse_y < 100):
						start = True
						total = total_secs
						print('press Start')
					if (300 < mouse_x < 450) and (150 < mouse_y < 200):
						total_secs = 0
						print('press Reset')
					print("total_secs = " + str(total_secs))

		if start:
			total_secs -= 1  # countdown
			if total_secs == 0:
				start = False
				pygame.mixer.Sound.play(sound)
			time.sleep(0.01)
			#time.sleep(1)

		if total_secs < 0:
			total_secs = 0

		mins = int(total_secs / 60)
		# secs = total_secs - (mins * 60)
		secs = int(total_secs % 60)

		time_now = str(mins) + ":" + str(secs)
		text_time = font.render(time_now, True, BLACK)  # set text
		screen.blit(text_time, (120, 120))  # show text

		x_sec = 250 + radius_secs * math.sin(6 * secs * math.pi / 180)
		y_sec = 400 - radius_secs * math.cos(6 * secs * math.pi / 180)
		pygame.draw.line(screen, BLACK, (250, 400), (int(x_sec), int(y_sec)))

		x_min = 250 + radius_mins * math.sin(6 * mins * math.pi / 180)
		y_min = 400 - radius_mins * math.cos(6 * mins * math.pi / 180)
		pygame.draw.line(screen, RED, (250, 400), (int(x_min), int(y_min)))

		# pass  # ignore
		if total != 0:
			pygame.draw.rect(screen, RED, (60, 530, int(380 * (total_secs/total)), 30))

		pygame.display.flip()  # show the color which was set before

	pygame.quit()

except Exception as bug:
	print(bug)
	input()  # to stop program