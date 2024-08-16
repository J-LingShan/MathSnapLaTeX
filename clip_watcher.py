import os
import time
import dashscope
import pyperclip
from PIL import ImageGrab
import linker
import infoProcess
import fileProcess
class Watcher:

    def __init__(self, model, Maas):
        self.model = model
        self.Maas = Maas
        self.refresh_time = 0.1
        self.temp_dir = './/temp'
        self.returnPath = f".//temp//temp.png"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

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
        while True:
            now_image = ImageGrab.grabclipboard()
            # 1.是截图 2.与上次截图不同 3.只有一张截图
            if now_image is not None and now_image != last_image and not isinstance(now_image, list):
                last_image = now_image
                # 监听成功则调用连接器
                if self.saveData(last_image):
                    response = linker.Linker(model=self.model,Maas=self.Maas,Watcher=self).Run()

                    response = infoProcess.InfoProcess().processResponse(response)
                    pyperclip.copy(f"{response}")
                    print(response)
                    fileProcess.FileProcess().delPath(self.returnPath)



            else:
                pass
            time.sleep(self.refresh_time)

    def modify_refresh_time(self, refresh_time):
        self.refresh_time = refresh_time





if __name__ == "__main__":
    Watcher(model='qwen-vl-plus',Maas=dashscope).monitor()