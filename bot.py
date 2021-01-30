from pyautogui import *
import pyautogui
import random
sleep(4)
print("go")
pyautogui.keyDown("space")
sleep(1)
pyautogui.keyUp("space")
pyautogui.keyUp("space")
for i in range(0,1000):
    seed = 0.62 + random.random() / 10

    print("round " + str(i) + " seed: " + str(seed) + " sell: " + str(i % 2 == 1))

    #Throw
    print("Throw") 
    pyautogui.keyDown("space")
    sleep(0.75 + -1 * seed / 10)
    pyautogui.keyUp("space")
    pyautogui.keyUp("space")
    pyautogui.press("space")
    #let sink 
    print("let sink") 
    sleep(1 + 2 * seed)

    #first pull
    pyautogui.keyDown("space")
    print("first pull")
    sleep(1 + 2 * seed)
    pyautogui.keyUp("space")
    pyautogui.keyUp("space")

    #let sink
    print("let sink 2") 
    sleep(1 + 1 * seed)
    #take in
    print("take in") 
    pyautogui.keyDown("space")
    sleep(7 + 7 * seed)
    pyautogui.keyUp("space")
    pyautogui.keyUp("space")

    #sell if big
    print("sell if big") 
    #if (i % 2 == 1):
        
    pyautogui.press("s")