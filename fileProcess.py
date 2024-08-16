import os
import shutil


class FileProcess:
    @staticmethod
    def init_file(paths):
        try:
            directory = os.path.dirname(paths)
            if not os.path.exists(directory):
                os.makedirs(directory)

            if not os.path.exists(paths):
                with open(paths,"w"):
                    pass
            # 创建文件
        except:
            print(">文件初始化异常")


    @staticmethod
    def setKeyValue(path,new_key, new_value):
        # print(f"key:{new_key},value:{new_value}")
        FileProcess.init_file(path)
        lines = []
        # try:
        with open(path,'r+',encoding='utf8') as files:
            isnew = True
            for line in files:
                if len(line.strip()) != 0:
                    key, value = line.strip().split('=')
                    if key == new_key:
                        new_line = f"{key}={new_value}"
                        isnew = False

                        # print(f'写入成功：{new_line}')
                    else:
                        new_line = line
                        # print(f"new_line:{new_line}")

                    lines.append(new_line)

                    # print(f"lines{lines}")

        #
        # if not lines:
        #     with open(path,'r+',encoding='utf8'):
        #         new_line = f"{new_key}={new_value}"
        #         lines.append(new_line)
        # print(lines)

        if isnew is True:
            new_line = f"{new_key}={new_value}"
            lines.append(new_line)

        return FileProcess.writeData(path,lines)

        # except:
        #     print("序列写入失败")
        #     return False


    @staticmethod
    # 键值对数据写入写入
    def writeData(path,lines):
        # try:
        file = open(path,"w",encoding='utf8')
        for i in lines:
            if not i.endswith('\n'):
                i += '\n'
            # print(f"i:{i}")
            file.write(i)
        file.close()
        return True
        # except:
        #     print("写入失败")
        #     return False

    @staticmethod
    def delPath(del_path):
        try:
            if os.path.isfile(del_path):
                # 删除文件
                os.remove(del_path)
            elif os.path.isdir(del_path):
                # 删除目录
                if os.listdir(del_path):  # 如果目录非空
                    shutil.rmtree(del_path)
                else:
                    os.rmdir(del_path)
            else:
                print(f">文件不存在{del_path}")
        except Exception as e:
            print(f">异常: {e}")

    @staticmethod
    def getKeyValue(find_path, find_key):
        try:
            with open(find_path, 'r+',encoding='utf8') as files:
                for line in files:
                    # print(f"{line}")
                    key, value = line.strip().split('=')
                    # print(f"{key},{find_key}")
                    if key == find_key:
                        return value

                return False
        except:
            return False





if __name__ == '__main__':
    path = "User Settings/config.txt"
    file = FileProcess().setKeyValue(path,'api_key','5')
    file2 = FileProcess().getKeyValue(path,'prompt')
    # print(file)
    # print(file2)