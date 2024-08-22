import os
import time
import webbrowser

import dashscope
import pyperclip
import requests
from PIL import ImageGrab
import linker
import infoProcess
import fileProcess
import app


class Watcher:

    def __init__(self, model, Maas):
        self.model = model
        self.Maas = Maas
        self.refresh_time = 0.1
        self.temp_dir = './/temp'
        self.returnPath = f".//temp//temp.png"
        self.heartbeat = "True"

        # 心跳检测
        self.isHeartbeat()
        if self.heartbeat == "False":
            print("Web心跳丢失")
            quit()
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

        url = "http://127.0.0.1:2024/"
        webbrowser.open(url, new=0, autoraise=True)
        linker.Linker(model=self.model,Maas=self.Maas,Watcher=self)

    def saveData(self,image):
        try:
            file_name = f"temp.png"
            self.file_path = os.path.join(self.temp_dir, file_name)
            image.save(self.file_path, 'PNG')
            print(">临时数据准备完毕")
            return True
        except:
            print(">Error:临时数据处理异常")
            return False

    def delData(self):
        try:
            os.remove(self.file_path)
            print(">Error:临时数据已删除")
            return True

        except:
            print(">Error:临时数据删除异常")
            return False
    def monitor(self):
        last_image = None
        print(f">监听中:{self.refresh_time}")
        self.isHeartbeat()

        while self.heartbeat == 'True':
            now_image = ImageGrab.grabclipboard()
            # 1.是截图 2.与上次截图不同 3.只有一张截图
            if now_image is not None and now_image != last_image and not isinstance(now_image, list):
                last_image = now_image
                # 监听成功则调用连接器
                if self.saveData(last_image):
                    response = linker.Linker(model=self.model,Maas=self.Maas,Watcher=self).Run()
                    url = 'http://127.0.0.1:2024/Request_Show'
                    response = infoProcess.InfoProcess().processResponse(response)
                    if response == 'Error:API_KEY exception':
                        requests.post(url=url,data={"Data":'Error:API_KEY exception'})
                        print(f"api异常")
                    else:
                        pyperclip.copy(f"{response}")
                        print(response)
                        requests.post(url=url,data={"Data":response})
                        fileProcess.FileProcess().delPath(self.returnPath)

            else:
                pass

            self.isHeartbeat()
            time.sleep(self.refresh_time)
        print("Web心跳丢失")

    def modify_refresh_time(self, refresh_time):
        self.refresh_time = refresh_time

    # 心跳检测
    def isHeartbeat(self):
        try:
            url = 'http://127.0.0.1:2024/heartbeat'
            result = requests.post(url=url, data='').text
            # print(f"Heartbeat:{result}")
            if result == "True":
                self.heartbeat = 'True'
            else:
                self.heartbeat = 'False'
        except:
            self.heartbeat = 'False'

if __name__ == "__main__":
    Watcher(model='qwen-vl-plus',Maas=dashscope).monitor()