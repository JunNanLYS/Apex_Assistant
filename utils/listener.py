from pynput import mouse, keyboard


class GameListener:
    def __init__(self):
        self.mouse_state = mouse.Listener(on_click=self._on_click)
        self.keyboard_state = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        self.is_close = False
        self._is_pause = False
        self._left_button = False
        self._right_button = False
        self._table = False

    @property
    def is_pause(self):
        return self._is_pause

    @property
    def in_bag(self):
        return self._table

    @property
    def left_down(self):
        return self._left_button

    @property
    def right_down(self):
        return self._right_button

    def _on_click(self, _x, _y, _button, _pressed):
        if _button == mouse.Button.left:
            self._left_button = _pressed
        elif _button == mouse.Button.right:
            self._right_button = _pressed

    def _on_press(self, _key):
        if _key == keyboard.Key.f8:
            self._is_pause = not self._is_pause
        elif _key == keyboard.Key.f10:
            self.is_close = True
        elif _key == keyboard.Key.tab:
            self._table = True

    def _on_release(self, _key):
        if _key == keyboard.Key.tab:
            self._table = False

    def start(self):
        self.mouse_state.start()
        self.keyboard_state.start()

    def stop(self):
        self.mouse_state.stop()
        self.keyboard_state.stop()
