import io
import os
from flask import Flask, send_file, send_from_directory,jsonify, request
import pyautogui
from PIL import Image
from diag import *

app = Flask(__name__,static_folder='www')

@app.route('/screenshot', methods=['GET'])
def screenshot():
    # 获取指定标题的窗口列表
    windows = getWindowList()
    
    # 检查是否找到窗口
    if not windows:
        return "Window not found", 404
    selection = int(request.args.get('selection'))

    # 获取窗口对象
    window = windows[selection]
    
    # 将窗口设为前台（可选）
    # if window.isMinimized:
    #     window.restore()
    # window.activate()

    try:
        # 直接截取窗口的区域，不使用 activate()
        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
    except Exception as e:
        return f"Error capturing screenshot: {e}", 500
    
    # 将截图保存到内存中
    img_io = io.BytesIO()
    screenshot.save(img_io, 'PNG')
    img_io.seek(0)

    # 返回截图作为响应
    return send_file(img_io, mimetype='image/png')

# 用于加载静态HTML文件
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.json
    x = data.get('x')
    y = data.get('y')
    selection = int(data['selection'])

    windows = getWindowList()
    
    # 检查是否找到窗口
    if not windows:
        return "Window not found", 404

    # 获取窗口对象
    window = windows[selection]

     # 计算绝对位置
    absolute_x = window.left + x
    absolute_y = window.top + y
    
    # 在这里可以执行点击操作，例如：
    pyautogui.click(absolute_x, absolute_y)
    
    return json.dumps({'status': 'success', 'absolute_x': absolute_x, 'absolute_y': absolute_y})


    try:
        # 模拟点击
        pyautogui.click(x, y)
        return jsonify({'message': 'Click simulated at ({}, {})'.format(x, y)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
