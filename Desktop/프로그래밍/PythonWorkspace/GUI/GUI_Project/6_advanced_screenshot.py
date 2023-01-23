import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

# 사용자가 F9를 누르면 스크린 샷 저장
keyboard.add_hotkey("F9", screenshot)

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행