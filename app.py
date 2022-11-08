import webbrowser
import pyautogui
import pyperclip
import time


webbrowser.open_new("https://www.google.com")


pyperclip.copy("あいうえお")
pyautogui.hotkey("command", "v")
pyautogui.press("enter")


time.sleep(5)
pyautogui.screenshot("screenshot_test_image.png")
screen_shot.save("test.png")
