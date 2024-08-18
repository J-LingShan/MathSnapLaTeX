import os
import sys
import dashscope

import fileProcess
import messages


class User:
    def __init__(self,model,MaaS):
        self.info = {'api_key': ''}
        self.path = 'User Settings/config.txt'
        self.path_prompt = 'User Settings/prompt'
        self.model = model
        self.MaaS = MaaS
        self.Messages = messages.Messages()
        self.parameter = {}  # 参数字典
        fileProcess.FileProcess.init_file(self.path)

        if getattr(sys,'frozen',False):
            path = os.path.join(sys._MEIPASS, 'User Settings/prompt')
            self.path_prompt = path
            self.set_DataFileTO_KeyValueDir('prompt', path)
        else:
            if fileProcess.FileProcess.init_file(self.path_prompt) == 'newFile':
                self.info["prompt"] = ' '

    def update(self):
        try:
            key = 'api_key'
            r1 = self.getKeyValue(key)
            r2 = self.getPrompt()

            if r1 is False or len(r1.strip()) == 0:
                api_key = input(f">info中未查询到key,请设置：")
                self.setKeyValueFile(api_key)
                print(">设置成功")

            elif r2 is False:
                print(">Error:prompt获取异常")
                return '>Error:prompt获取异常'

            else:
                self.info[key] = r1
                self.info['prompt'] = r2
        except FileNotFoundError as e:
            print(f'>数据文件异常：{e}')

    def reset_default(self):
        self.info = {'api_key': ''}
        fileProcess.FileProcess.delPath('User Settings')

    def getKeyValue(self,key='api_key',path=None):
        if path is None:
            path = self.path
        result = fileProcess.FileProcess().getKeyValue(path,key)
        if result is not False:
            return result
        else:
            return False

    def getPrompt(self,path_prompt=None):
        if path_prompt is None:
            path_prompt = self.path_prompt
        return self.getKeyValue("prompt", path_prompt)

    def setPromptFile(self, prompt, path_prompt=None):
        if path_prompt is None:
            path_prompt = self.path_prompt
        return fileProcess.FileProcess().setKeyValue(path_prompt,new_key='prompt',new_value=prompt)

    def setKeyValueFile(self,value,key='api_key', path=None):
        if path is None:
            path = self.path
        return fileProcess.FileProcess().setKeyValue(path,new_key=key,new_value=value)

    def setKeyValueDir(self, key, value):
        self.info[key] = value

    def set_DataFileTO_KeyValueDir(self,key,path):  # 通过文件对info进行赋值
        value = self.getKeyValue(key, path)
        if value is not False:
            self.info[key] = value


if __name__ == '__main__':
    User = User(model='qwen-vl-plus',MaaS=dashscope)
    # print(settings.get_key("api_key"))

    print(User.setKeyValueFile('123'))
    print(User.setPromptFile("哈"))




