import pyautogui
import random

from PIL import Image

from diag import *
from diag_func import *

print("Hello World!")

sz = pyautogui.size()
random_increase = random.randint(-4, 4)

print("11111:", random_increase)


diags = getWindowList()
print(diags)

for diag in diags:
    diag.leftClickImg("test", yfix=50)

print(111111111111111)
