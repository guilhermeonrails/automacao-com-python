import pyautogui
from time import sleep

sleep(2)
pyautogui.moveTo(x=45, y=52)
pyautogui.click()
sleep(2)
pyautogui.click(1730, 12)
pyautogui.write('visual', interval=0.2)
pyautogui.press('enter')
# print(pyautogui.position())