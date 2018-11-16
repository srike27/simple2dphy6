import pygame

pygame.init()
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

c = pygame.joystick.get_count()
joystick = pygame.joystick.Joystick(0)
joystick.init()
n = joystick.get_numaxes()
print n

while(c):
	joystick.get_axis(0)
	joystick.get_axis(1)
	joystick.get_axis(2)
	joystick.get_axis(3)

	print "\n\n\n\n\n\n"
	clock.tick(20)
pygame.quit()
