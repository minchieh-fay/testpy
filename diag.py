import argparse
import pyautogui
import sys


import tool
import diag_func

windowsList = None
def getWindowList():
    global windowsList
    if windowsList is not None:
        return windowsList
    if tool.TEST_MODE:
        windowsList = pyautogui.getWindowsWithTitle('Calculator')
    else:
        windowsList = pyautogui.getWindowsWithTitle('梦幻西游：时空')
    
    windowsList = list(filter(lambda x: x.left >= 0, windowsList))
    windowsList.sort(key=lambda x: (x.left, x.top))

    if windowsList is None:
        print("没有找到窗口")
        tool.mySleep(10)
        sys.exit(1)

    diagmove()

    for item in windowsList:
        diag_func.diag_func(item)

    return windowsList

def diagmove():
    size = tool.smallSize
    winList = getWindowList()
    sz = pyautogui.size()
    x0 = size[0] - 15
    l = int((sz.width - 2 * x0) / 2)
    zhuomianban = (l, l + x0, l, l + x0, int((sz.width - size[0]) / 2))
    i = 0
    
    for idx, item in enumerate(winList):
        tool.log(item)
        item.resizeTo(size[0], size[1])
        tool.mySleep(1)
        if idx == 4:
            item.moveTo(zhuomianban[4], int((sz.height - size[1]) / 2))
        else:
            # 这里任务栏写死36
            no2LineTop = (sz.height - size[1] - 36 if sz.height - size[1] * 2 < 0 else size[1]) * int(i / 2)
            item.moveTo(zhuomianban[i], no2LineTop)
            i += 1
        tool.log("处理后：", item)


if __name__ == '__main__':
    diagmove()