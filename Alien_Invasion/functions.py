import sys
import pygame

def check_events():
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()