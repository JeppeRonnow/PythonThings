import pyautogui as auto
import pyscreenshot as imggrab
from time import sleep

def load_status():
    global load
    load = 1
    global i
    i = 0


    while load == 1:
        img = imggrab.grab(bbox=(841, 784, 841+1, 784+1))
        img2 = imggrab.grab(bbox=(950, 866, 950+1, 866+1))

        i = i + 1
        print(i)
        
        rgb_pixel_value = img.getpixel((0, 0))
        rgb_pixel_value2 = img2.getpixel((0, 0))

        if rgb_pixel_value == (255,255,255) and rgb_pixel_value2 == (234,238,178):
            load = 0
            return True
        

def main():

    if load_status() == True:
        lockin()
        print("agent locked")
        

def lockin():
    auto.click(626, 925)
    auto.click(clicks=2)
    sleep(0.02)
    auto.moveTo(1085,820)
    auto.drag(-15,0,duration=0.02)
    auto.click(clicks=2)


main()