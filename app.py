import pyautogui
import webbrowser
import time


# webbrowser.open("https://google.com")
webbrowser.open_new("https://www.google.com")


time.sleep(1)

pyautogui.press("h")
pyautogui.press("i")
pyautogui.press("r")
pyautogui.press("a")
pyautogui.press("i")
pyautogui.press("z")
pyautogui.press("u")
pyautogui.press("m")
pyautogui.press("i")
pyautogui.press("c")
pyautogui.press("y")
pyautogui.press("o")
pyautogui.press("u")
pyautogui.hotkey("space", "Enter")
pyautogui.press("k")
pyautogui.press("a")
pyautogui.press("n")
pyautogui.press("k")
pyautogui.press("o")
pyautogui.press("u")
pyautogui.hotkey("space", "Enter", "Enter")
pyautogui.screenshot("screenshot_test_image.png")
