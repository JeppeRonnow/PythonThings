from PIL import ImageGrab as imggrab
from playsound import playsound 
import os

def hasBomb() -> bool:
    img = imggrab.grab(bbox=(1850, 686, 1850+1, 686+1))

    rgb_pixel_value = img.getpixel((0, 0))
    
    if rgb_pixel_value == (255,255,255):
        return True
    return False

def main():
    cwd = os.getcwd()

    print("Script armed and ready")
    while True:
        if hasBomb():
            print("Smid den fucking Spike")
            playsound(cwd + "\Kampp.wav") 

if __name__ == "__main__":
    main()
