import pygame


pygame.init()

done = False

clock = pygame.time.Clock()

pygame.joystick.init()
    
while done==False:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 
        
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    joystick_count = pygame.joystick.get_count()


    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        name = joystick.get_name()
        
        axes = joystick.get_numaxes()
        
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            
            
        buttons = joystick.get_numbuttons()
        

        for i in range( buttons ):
            button = joystick.get_button( i )
           
        hats = joystick.get_numhats()
       

        for i in range( hats ):
            hat = joystick.get_hat( i )
        
    clock.tick(20)
pygame.quit ()
