import pyautogui
import random
import threading
from PIL import Image

import tool
import diag
import diag_func

print("Hello World!")

mibaotu_thread = None
mibaotu_running = False


def run_mi_tu_do():
  ds = diag.getWindowList()
  while True:
    for d in ds:
      tool.mySleep(5)
      if not mibaotu_running:
        continue
      if tool.TEST_MODE:
        print("Testing mode,run_mi_tu_do:", mibaotu_running)
        continue
      d.leftClickImg("baotu_wa", yfix=41)
      tool.mySleep(5)
      d.leftClickImg("mijin_zhandou")

def run_mi_tu(run=False):
  global mibaotu_thread
  global mibaotu_running
  mibaotu_running = run
  if mibaotu_thread is None:
    mibaotu_thread = threading.Thread(target=run_mi_tu_do)
    mibaotu_thread.start()

if __name__ == '__main__':
  mibaotu_running = True
  run_mi_tu_do()