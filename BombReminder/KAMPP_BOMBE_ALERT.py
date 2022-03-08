from PIL import ImageGrab as imggrab
from playsound import playsound 

def hasBomb() -> bool:
    img = imggrab.grab(bbox=(1850, 686, 1850+1, 686+1))

    rgb_pixel_value = img.getpixel((0, 0))
    
    if rgb_pixel_value == (255,255,255):
        return True
    return False

def main():
    while True:
        if hasBomb():
            playsound("BombReminder\Kampp.wav")
            

if __name__ == "__main__":
    main()
