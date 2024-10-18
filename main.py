import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()

	clock = pygame.time.Clock()
	dt = 0
	score = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Player.containers = (updatable, drawable)
	Shot.containers = (updatable, drawable, shots)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	font = pygame.font.Font('freesansbold.ttf', 32)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			for shot in shots:
				if asteroid.check_collision(shot):
					score += 1
					asteroid.split()
					shot.kill()
			if asteroid.check_collision(player):
				print("Game over!")
				sys.exit()

		pygame.Surface.fill(screen, color = 'black')
		text = font.render(f"Score: {score}", True, 'white')
		textRect = text.get_rect()
		screen.blit(text, textRect)
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# limit framerate to 60 fps
		dt = clock.tick(60) / 1000

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
	main()
