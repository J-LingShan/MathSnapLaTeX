import dashscope
import webbrowser
import apple
from clip_watcher import Watcher


if __name__ == "__main__":
    url = "http://127.0.0.1:2024/"
    webbrowser.open(url, new=0, autoraise=True)
    Watcher(model='qwen-vl-plus',Maas=dashscope).monitor()

