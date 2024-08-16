
class Messages:
    def __init__(self):
        self.role = ''
        self.content = []
        self.messages = []

    def setRole(self, role):
        self.role = role

    def set_content(self,content_type,content_info):
        # 构造content
        dir_content = {content_type:content_info}
        self.content.append(dir_content)

    def set_messages(self):
        dir_message = {'role': self.role, 'content': self.content}
        # 构造一次消息(role+content)载入message列表里
        self.messages.append(dir_message)

    def getMessages(self):
        return self.messages

    def all_operate(self,role,content_type,content_info):
        self.setRole(role)
        # self.set_content(content_type,content_info) # 不能再加这个，不然会再重复加一遍，会多出：{'text': [...]}]}]
        self.set_messages()
        self.getMessages()





