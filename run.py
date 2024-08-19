import dashscope

import apple
from clip_watcher import Watcher


if __name__ == "__main__":
    Watcher(model='qwen-vl-plus',Maas=dashscope).monitor()
    apple.run()
