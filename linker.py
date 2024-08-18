import dashscope
from dashscope.common.error import UploadFileException

import clip_watcher
import settings
import messages
import agents


class Linker:
    def __init__(self,model,Maas,Watcher):
        self.User = settings.User(model,Maas)
        self.User.update()
        self.Watcher = Watcher


    def Run(self):
        # 初始化
        self.User.update()

        # content封装
        # print(f"测试：{self.Watcher.returnPath}")
        self.User.Messages.set_content('image',self.Watcher.returnPath)
        self.User.Messages.set_content('text',self.User.getPrompt())
        # print(self.User.Messages.getMessages())

        # message的封装
        self.User.Messages.all_operate('user','text',self.User.Messages.content)
        # print(self.User.Messages.messages)

        # 加载agent
        res = self.request()

        # print(f'zg:{res}')
        return res

    '''
        测试
        r = self.all_operates("user",'text',"你是谁")
        print(r)
    '''

    # def setMessages(self, role, content_type, content_info):
    #     self.User.Messages.all_operate(role,content_type,content_info)

    def request(self):
        try:
            Agent = agents.Agent(self.User)
            response = Agent.request_agent()

            return response
        except self.User.MaaS.common.error.UploadFileException as e:
            print(f">Error：{e}")
            quit()

    # def all_operates(self, role, content_type, content_info):
    #     self.setMessages(role, content_type, content_info)
    #     return self.request()


    # def request(self, m=1):
    #     Agent = agents.Agent()
    #     if m == 1:
    #         response = Agent.request_agent()
    #     else:
    #         response = Agent.request_agent_dir(self.parameter)
    #
    #     return response


if __name__ == '__main__':
    linker = Linker(model='qwen-vl-plus',Maas=dashscope)
