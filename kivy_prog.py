import kivy

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        def add_button(text, size_x, size_y, pos_x, pos_y):
            self.add_widget(
                Button(
                    text=text,
                    font_size=24,
                    size_hint=(size_x, size_y),
                    pos_hint={'center_x':pos_x, 'center_y':pos_y}))

        add_button("NUM\nLOCK", 1/4, 1/5, 1/8, 9/10)
        add_button('/', 1/4, 1/5, 3/8, 9/10)
        add_button('*', 1/4, 1/5, 5/8, 9/10)
        add_button('-', 1/4, 1/5, 7/8, 9/10)
        add_button('7', 1/4, 1/5, 1/8, 7/10)
        add_button('8', 1/4, 1/5, 3/8, 7/10)
        add_button('9', 1/4, 1/5, 5/8, 7/10)
        add_button('4', 1/4, 1/5, 1/8, 5/10)
        add_button('5', 1/4, 1/5, 3/8, 5/10)
        add_button('6', 1/4, 1/5, 5/8, 5/10)
        add_button('1', 1/4, 1/5, 1/8, 3/10)
        add_button('2', 1/4, 1/5, 3/8, 3/10)
        add_button('3', 1/4, 1/5, 5/8, 3/10)
        add_button('+', 1/4, 2/5, 7/8, 6/10)
        add_button("ENTER", 1/4, 2/5, 7/8, 2/10)
        add_button('0', 2/4, 1/5, 2/8, 1/10)
        add_button('.', 1/4, 1/5, 5/8, 1/10)
        

class MainApp(App):
    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(.1, .1, .1, .1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root


    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == "__main__":
    MainApp().run()
