import pyautogui
import os
import time

path="E:// Screenshot"
# os.mkdir(path)

for i in range(10):
    time.sleep(3);

    filename=f"mera_screenshot{i}.jpg"
    filepath=os.path.join(path,filename)
    screenshot=pyautogui.screenshot()
    screenshot=pyautogui.screenshot()
    screenshot.save(filepath)
print("ho gya kaam")