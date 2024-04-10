from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from PDFReader import PDFReader
from StringGroupingSystem import StringGroupingSystem
from StringSelectingSystem import StringSelectingSystem
import re


class CustomScrollView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = None
        self.bind(scroll_y=self.on_scroll_y)

    def on_scroll_y(self, instance, value):
        if self.label:
            self.label.height = max(self.label.parent.height, self.label.texture_size[1])


class CustomLabel(Label):
    pass


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        label = Label(text="Chcesz pogrupować wyniki po zawodnikach czy po dystansach?")
        layout.add_widget(label)

        # Przyciski do wyboru
        button_athletes = Button(text='Zawodnicy', on_press=self.on_button_athletes_press)
        button_distances = Button(text='Dystanse', on_press=self.on_button_distances_press)

        # Dodawanie przycisków do interfejsu
        layout.add_widget(button_athletes)
        layout.add_widget(button_distances)

        return layout

    def on_button_athletes_press(self, instance):
        self.number = 1
        self.process_choice()

    def on_button_distances_press(self, instance):
        self.number = 2
        self.process_choice()

    def process_choice(self):
        text_to_operate_on = PDFReader.get_text_from_pdf()  # Assuming this method returns a list of text chunks
        chunks_of_text = []
        one_chunk_of_text = ""

        for text in text_to_operate_on:
            if re.match(r'[\w-]+\s+\w+,\s+\d+\s+', text) or text == text_to_operate_on[-1] or re.match(
                    r'[\w-]+\s+\w+\s+,\s+\d+\s+', text):
                chunks_of_text.append(one_chunk_of_text)
                one_chunk_of_text = ""
            one_chunk_of_text += text + "\n"

        # Call the appropriate methods for grouping and selecting important strings
        output_text = StringGroupingSystem.group_by(StringSelectingSystem.select_important_string(chunks_of_text),
                                                    self.number)
        print(output_text)
        output_label = Label(text=output_text)

        # Create a new window to display the output
        popup_layout = GridLayout(cols=1)
        output_label = CustomLabel(text=output_text, size_hint_y=None)
        scroll_view = CustomScrollView(size_hint=(1, 0.9))
        scroll_view.label = output_label
        scroll_view.add_widget(output_label)
        popup_layout.add_widget(scroll_view)

        popup = Popup(title='Output', content=popup_layout, size_hint=(None, None), size=(400, 400))
        popup.open()


if __name__ == "__main__":
    MainApp().run()
