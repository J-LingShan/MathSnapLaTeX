import json

class InfoProcess:

    def __init__(self):
        self.response = ''

    def wrap_with_dollars(self,text):
        # 检查字符串是否已经以 $ 开头和结尾
        if not (text.startswith('$') and text.endswith('$')):
            # 如果不是，则添加 $
            # print("没有美元符号")
            text = f'$${text}$$'

        return text

    def processResponse(self,response):
        text = json.loads(str(response))['output']['choices'][0]['message']['content'][0]['text']
        return self.wrap_with_dollars(text)



