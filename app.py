import webbrowser
import pyautogui
import pyperclip
import time

# GUIで
webbrowser.open_new_tab("https://www.google.com/")
time.sleep(1)
# left, top, width, height = pyautogui.locateOnScreen("google.png", confidence=0.1)
# pyautogui.click(left, top)
# pyautogui.click(382, 269)
pyperclip.copy("平泉町　観光")
pyautogui.keyDown("command")
pyautogui.press("v")
pyautogui.keyUp("command")
pyautogui.press("Enter")
time.sleep(3)
pyautogui.screenshot("screenshot.png")
