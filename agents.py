import settings
import messages
import fileProcess

class Agent:
    def __init__(self,User):
        self.User = User
        self.setParameter("top_p",0.01)

    # 无字典参数传递
    def request_agent(self):
        model = self.User.model
        message = self.User.Messages.getMessages()
        # print(f"message{message}")
        # print(f'zg{self.User.MaaS.api_key}')
        self.User.MaaS.api_key = self.User.getKeyValue()

        MaaS_2 = self.User.MaaS.MultiModalConversation
        response = MaaS_2.call(model=model, messages=message)

        # print(f"response{response}")
        return response

    def request_agent2(self):
        parameter = self.User.parameter
        self.request_agent_dir(parameter)

    def setParameter(self, parameter_name, parameter_value):
        self.User.parameter[parameter_name] = parameter_value

    def request_agent_dir(self, param_dict, **kwargs):
        kwargs.update(param_dict)
        model = self.User.model
        message = self.User.Messages.getMessages()
        print(f"message{message}")
        self.User.MaaS.api_key = self.User.getKeyValue()
        MaaS_2 = self.User.MaaS.MultiModalConversation
        response = MaaS_2.call(model=model, messages=message,**kwargs)
        print(f"response{response}")
        return response
















