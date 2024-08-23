import os
import subprocess
import time

import requests

# 获取当前脚本所在的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))
bat_dir = os.path.join(script_dir, "system")


# 创建 batch 文件
bat = [
    "@echo off",
    "setlocal",
    "",
    ":: 指定要运行的可执行文件路径",
    'set "run1_exe=run1.exe"',
    'set "run2_exe=run2.exe"',
    "",
    ":: 运行第一个程序",
    'echo Running %run1_exe%',
    'start "" "%run1_exe%"',
    "",
    ":: 等待1秒",
    'timeout /t 1 >nul',
    "",
    ":: 运行第二个程序",
    'echo Running %run2_exe%',
    'start "" "%run2_exe%"',
    "",
    "endlocal"
]

# 指定bat文件的路径
bat_file = os.path.join(bat_dir, "MathSnapLaTeX.bat")

# 确保目标目录存在
directory = os.path.dirname(bat_file)
if not os.path.exists(directory):
    os.makedirs(directory)

# 写入 batch 文件
with open(bat_file, "w+", encoding="utf-8") as file:
    for line in bat:
        file.write(line + '\n')

# 使用 subprocess.run 来运行 bat 文件
subprocess.run([bat_file], cwd=bat_dir)  # 指定脚本所在目录为工作目录


def isHeartbeat():
    try:
        url = 'http://127.0.0.1:2024/heartbeat'
        result = requests.post(url=url, data='').text
        print(f"Heartbeat:{result}")
        if result == "True":
            # print("我已经收到心脏信号了")
            return 'True'
        else:
            return 'False'
    except:
        return 'False'

time.sleep(5)
while isHeartbeat() == 'True':
    time.sleep(5)




