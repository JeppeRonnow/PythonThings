import pyautogui as auto
import pyscreenshot as imggrab
from time import sleep


def agentSel():
    slotInput = input("Select agent slot number: ")
    if slotInput.strip().isdigit():
        slotInput = int(slotInput)
    else:
        print("Not a number")
        quit()

    while 1 < slotInput > 18:
        print("Ivalid number, has to be between 1-18")
        slotInput = int(input("Select agent slot number: "))

    global agent_X
    agent_X = 626

    global agent_Y
    agent_Y = 925

    if slotInput == 1:
        agent_X = agent_X
    elif slotInput > 1 and slotInput < 10:
        agent_X = agent_X+84*(slotInput-1)
    elif slotInput > 9 and slotInput < 19:
        agent_X = agent_X+84*(slotInput-10)
        agent_Y = agent_Y + 84

def load_status():
    global load
    load = True

    while load == 1:
        img = imggrab.grab(bbox=(841, 784, 841+1, 784+1))
        img2 = imggrab.grab(bbox=(950, 866, 950+1, 866+1))

        rgb_pixel_value = img.getpixel((0, 0))
        rgb_pixel_value2 = img2.getpixel((0, 0))

        if rgb_pixel_value == (255,255,255) and rgb_pixel_value2 == (234,238,178):
            load = False
            return True
        

def main():
    agentSel()

    if load_status() == True:
        lockin()
        print("agent locked")
        sleep(2)
        quit()
        
def lockin():
    auto.click(agent_X, agent_Y)
    auto.click(clicks=1)
    sleep(0.02)
    auto.moveTo(1085,820)
    auto.drag(-15,0,duration=0.02)
    auto.click(clicks=2)

main()