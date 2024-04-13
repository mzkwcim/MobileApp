from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
import pyperclip


class CustomScrollView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output_label = Label(text='', size_hint_y=None, markup=True, width=self.width)
        self.add_widget(self.output_label)

    def update_output_text(self, text):
        self.output_label.text = text
        self.output_label.texture_update()
        self.output_label.text_size = (500, None)
        self.output_label.size = self.output_label.texture_size

    def copy_to_clipboard(self, instance):
        pyperclip.copy(self.output_label.text)

