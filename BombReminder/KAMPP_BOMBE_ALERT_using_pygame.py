from PIL import ImageGrab as imggrab
import pygame
import os
from time import sleep

def BombSound():
    cwd = os.getcwd()
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(cwd + "\Kampp.wav")
    sound.set_volume(1)  
    sound.play() 

def hasBomb() -> bool:
    img = imggrab.grab(bbox=(1850, 686, 1850+1, 686+1))

    rgb_pixel_value = img.getpixel((0, 0))
    
    if rgb_pixel_value == (255,255,255):
        return True
    return False

def main():
    print("Script armed and ready")
    while True:
        if hasBomb():
            print("Smid den fucking Spike")
            BombSound()
            sleep(4)

if __name__ == "__main__":
    main()
