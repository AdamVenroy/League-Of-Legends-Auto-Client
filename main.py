import pyautogui
import time
import os
import cv2

current_dir = os.path.dirname(os.path.realpath(__file__)) 
champion_dir = current_dir + "\\champion\\"
TIME_CONSTANT = 0.1
#1600 x 900 : 80x80 img
#1280 x 720: 64x64 img

def move_mouse_to_champion(champion):
    """Moves mouse to champion (assuming champion is on screen)
    Returns True if image is found, otherwise false.
    """
    image_dir = champion_dir + champion + ".png"
    image = cv2.imread(image_dir)
    image = cv2.resize(image, (64, 64))
    image = pyautogui.locateOnScreen(image, confidence=0.55)
    is_image_found = image is not None
    if is_image_found:
        x = image.left + image.width // 2
        y = image.top + image.height // 2
        pyautogui.moveTo(x, y)
    
    return is_image_found


def find_champion(champion):
    """Scrolls through champions in champ select and clicks the champion"""
    image_dir = champion_dir + champion + ".png"
    image = cv2.imread(image_dir)
    image = cv2.resize(image, (64, 64))
    move_mouse_to_champion("Aatrox")
    while move_mouse_to_champion(champion) is False:
        pyautogui.scroll(-200)

def main():
    '''
    i = 0
    champion = "Zac"
    image_dir = champion_dir + champion + ".png"
    image = cv2.imread(image_dir)
    image = cv2.resize(image, (64, 64))
    while True:
        x = pyautogui.locateOnScreen(image, confidence=0.5)
        is_found = x is not None
        if is_found:
            print(f"{i}: found")
            print(x)
        else:
            print(f"{i}: not found")
        i += 1
        time.sleep(TIME_CONSTANT)
    '''
    find_champion("Zac")

main()
