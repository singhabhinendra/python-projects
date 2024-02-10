print("hello")  ##Python auto GUI and time module.
import pyautogui
import time
print("Aaj to mna k rhunga")
def message_sender(message):
    time.sleep(1)
    pyautogui.typewrite(message,interval=0.3)
    pyautogui.press("enter")


message ="i'll be your drink will you be chakhna i love you darling dhyaan rakhna apna !"
message_sender(message)  




    
    