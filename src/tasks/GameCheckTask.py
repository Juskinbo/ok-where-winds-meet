from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class GameCheckTask(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Game Check"
        self.description = "Capture the current frame and report the game window resolution and status."
        self.icon = FluentIcon.HEART
        self.default_config.update({
            "Wait For Game": True,
            "Wait Timeout": 60,
        })
        self.config_description.update({
            "Wait For Game": "Keep waiting until a frame can be captured.",
            "Wait Timeout": "Maximum seconds to wait before giving up.",
        })

    def run(self):
        wait = self.config.get("Wait For Game", True)
        timeout = self.config.get("Wait Timeout", 60)
        if wait:
            frame = self.wait_until(self.next_frame, time_out=timeout)
        else:
            frame = self.next_frame()
        if frame is None:
            self.log_warning("Could not capture the game window.")
            self.info_set("Game Window", "Not Found")
            return
        height, width = frame.shape[:2]
        self.info_set("Game Window", "Running")
        self.info_set("Resolution", f"{width}x{height}")
        self.log_info("Game check completed.", notify=True)
