from ok import BaseTask


class AutoPoison(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动刷毒"
        self.description = ""
        self.instructions = """<a href="https://github.com/ok-oldking/ok-py">ok-py</a>"""

        self.capture_config = {
            'windows': {
                'exe': 'yysls.exe',
                'hwnd_class': '79b5qjw29fL50Ku',
                'interaction': 'Pynput',
                'capture_method': 'WGC',
                # 'resolution': (2560, 1440),
            }
        }

    def run(self):
        while True:  # 无限循环按键，直到用户手动停止任务。
            self.send_key('1', down_time=0.12, after_sleep=1.60)  # 按一次数字 1，之后等待 1.60 秒。
            self.send_key('q', down_time=0.07, after_sleep=0.10)  # 按一次 q，之后等待 0.10 秒。
            self.send_key('q', down_time=0.08)  # 按一次 q。
            self.send_key('q', down_time=0.07)  # 按一次 q。
            self.send_key('q', down_time=0.07)  # 按一次 q。
            self.send_key('q', down_time=0.07)  # 按一次 q。
            self.send_key('q', down_time=0.06)  # 按一次 q。
            self.send_key('q', down_time=0.07)  # 按一次 q。
            self.send_key('q', down_time=0.09)  # 按一次 q。
            self.send_key('q', down_time=0.08, after_sleep=1.01)  # 按一次 q，之后等待 1.01 秒。
            self.send_key('space', down_time=1.25, after_sleep=0.33)  # 按一次空格，之后等待 0.33 秒。
            self.send_key('space', down_time=0.49, after_sleep=3.67)  # 按一次空格，之后等待 3.67 秒。
            self.send_key('q', down_time=0.10)  # 按一次 q。
            self.sleep(0.5)  # 每轮结束后的停顿，让出执行权并响应手动停止。