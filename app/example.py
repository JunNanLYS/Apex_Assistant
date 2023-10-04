import time

import win32api
import win32con

from utils import GameListener

"""
This is Apex assistant example.
F8 is pause
F10 is close Apex assistant
Press the left and right buttons at the same time start Assisted aiming
"""


class ApexAssistant:
    def __init__(self, radius=5):
        x = y = radius
        self.listener = GameListener()
        self.listener.start()
        self.positions = [
            (-x, 0), (0, -y), (x, 0), (x, 0),
            (0, y), (0, y), (-x, 0), (-x, 0),
            (0, -y), (x, 0)
        ]
        self.idx = 0

    def run(self):
        while not self.listener.is_close:
            if self.listener.is_pause:
                time.sleep(0.3)
                continue
            if self.listener.right_down and self.listener.left_down:
                x, y = self.positions[self.idx % len(self.positions)]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
                self.idx += 1
            else:
                time.sleep(0.3)
            time.sleep(0.01)


if __name__ == "__main__":
    assistant = ApexAssistant()
    assistant.run()
