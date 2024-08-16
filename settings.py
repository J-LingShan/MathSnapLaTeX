import os

import dashscope

import fileProcess
import messages


class User:
    def __init__(self,model,MaaS):
        self.info = {'api_key': ''}
        self.path = 'User Settings/config.txt'
        self.model = model
        self.MaaS = MaaS
        self.Messages = messages.Messages()
        self.parameter = {}  # 参数字典
        fileProcess.FileProcess.init_file(self.path)

    def update(self):
        try:
            key = 'api_key'
            r1 = self.getKeyValue(key)
            r2 = self.getPrompt()

            if r1 is False or len(r1.strip()) == 0:
                api_key = input(f">info中未查询到key,请设置：")
                self.setKeyValue(api_key)
                print(">设置成功")

            elif r2 is False:
                return '>prompt获取失败'

            else:
                self.info[key] = r1
                self.info['prompt'] = r2
        except FileNotFoundError as e:
            print(f'>数据文件异常：{e}')



    def reset_default(self):
        self.info = {'api_key': ''}
        fileProcess.FileProcess.delPath('User Settings')

    def getKeyValue(self,key='api_key'):
        result = fileProcess.FileProcess().getKeyValue(self.path,key)
        if result is not False:
            return result
        else:
            return False

    def getPrompt(self):
        return self.getKeyValue("prompt")

    def setPrompt(self,prompt):
        return fileProcess.FileProcess().setKeyValue(self.path,new_key='prompt',new_value=prompt)

    def setKeyValue(self,value,key='api_key'):
        return fileProcess.FileProcess().setKeyValue(self.path,new_key=key,new_value=value)


if __name__ == '__main__':
    User = User(model='qwen-vl-plus',MaaS=dashscope)
    # print(settings.get_key("api_key"))

    print(User.setKeyValue('123'))
    print(User.setPrompt("哈"))




