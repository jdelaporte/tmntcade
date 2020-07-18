#!/usr/bin/env python3
"""Four Player invaders clone."""

import pygame
from sprites import TextPrint, ControlSet, Player

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

textPrint = TextPrint()

# Initialize the joysticks
pygame.init()
pygame.joystick.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Inv4ders")
pygame.mouse.set_visible(False)

class Invaders():
    """Game loggic goes here."""
    done = False

    player1 = Player(screen=screen, color=YELLOW,
                     controls=[ControlSet(), ControlSet(up=pygame.K_w, down=pygame.K_s,
                                                        left=pygame.K_a, right=pygame.K_d)])
    player2 = Player(screen=screen, color=RED,
                     controls=[ControlSet(up=pygame.K_j, down=pygame.K_k,
                                          left=pygame.K_h, right=pygame.K_l)])
    player3 = Player(screen=screen, color=BLUE,
                     controls=[ControlSet(up=pygame.K_3, down=pygame.K_2,
                                          left=pygame.K_1, right=pygame.K_4)])
    player4 = Player(screen=screen, color=PURPLE,
                     controls=[ControlSet(up=pygame.K_7, down=pygame.K_6,
                                          left=pygame.K_5, right=pygame.K_8)])

    def controls(self):
        """Check for control inputs."""

        # Keyboard controls - for testing without joysticks

        # events = pygame.event.get()

        keys = pygame.key.get_pressed()
        self.player1.control(keys=keys)
        self.player2.control(keys=keys)
        self.player3.control(keys=keys)
        self.player4.control(keys=keys)

        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()

        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Exit like RetroArch - any joystick
            button7 = joystick.get_button(7)
            button8 = joystick.get_button(8)
            if button7 == button8 == 1:
                self.done = True

            if i == 0:
                self.player1.control(joystick=joystick)
            if i == 1:
                self.player2.control(joystick=joystick)
            if i == 2:
                self.player3.control(joystick=joystick)
            if i == 3:
                self.player4.control(joystick=joystick)

    def logic(self):
        """Calculate game logic."""
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def draw(self):
        """Update the screen."""
        # --- Drawing
        # Set the screen background

        self.player1.draw()
        self.player2.draw()
        self.player3.draw()
        self.player4.draw()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        textPrint.reset()
        screen.fill(WHITE)
        joystick_count = pygame.joystick.get_count()
        textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))

# -------- Main Program Loop -----------
inv = Invaders()
while not inv.done:
    inv.controls()
    inv.logic()
    inv.draw()
    # Limit to 60 frames per second
    clock.tick(60)

# Close everything down
pygame.quit()
