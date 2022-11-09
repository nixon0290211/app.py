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
pyautogui.hotkey("Ctrl", "v")
pyautogui.press("enter")
time.sleep(2)
pyautogui.screenshot("screenshot.png")

# セレニウム
# from selenium import webdriver
# driver = webdriver.Chrome()








# import webbrowser
# import pyautogui
# import pyperclip
# import time


# webbrowser.open_new("https://www.google.com")

# time.sleep(3)
# pyperclip.copy("平泉町 観光")
# pyautogui.hotkey("command", "v")
# pyautogui.press("enter")


# time.sleep(5)
# pyautogui.screenshot("screenshot_test_image.png")
