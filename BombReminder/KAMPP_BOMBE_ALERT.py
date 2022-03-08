from PIL import ImageGrab as imggrab
from pydub import AudioSegment
from pydub.playback import play

def hasBomb() -> bool:
    img = imggrab.grab(bbox=(1850, 686, 1850+1, 686+1))

    rgb_pixel_value = img.getpixel((0, 0))
    
    if rgb_pixel_value == (255,255,255):
        return True
    return False

def main():
    print("gfdgd")
    while True:
        if hasBomb():
            song = AudioSegment.from_mp3("KAMPP!.mp3")
            play(song)
            print("hej")

if __name__ == "__main__":
    main()
