from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.clock import mainthread
from kivy.uix.popup import Popup
import re
from PDFReader import PDFReader
from StringGroupingSystem import StringGroupingSystem
from StringSelectingSystem import StringSelectingSystem
from CustomScrollView import CustomScrollView


class PDFParserApp(App):
    def __init__(self, **kwargs):
        super(PDFParserApp, self).__init__(**kwargs)
        self.layout = None
        self.file_chooser = None
        self.file_path_label = None

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.current_view = None

        self.file_chooser = FileChooserListView(filters=["*.pdf"])
        select_button = Button(text="Select File", size_hint=(1, None), height=50)
        select_button.bind(on_press=self.display_grouping_options)

        self.file_path_label = Label(text="")

        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(select_button)
        self.layout.add_widget(self.file_path_label)

        return self.layout

    @mainthread
    def display_grouping_options(self, instance):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0] or ""
        if selected_file:
            self.layout.clear_widgets()

            self.file_path_label.text = selected_file
            self.layout.add_widget(self.file_path_label)

            label = Label(text="Chcesz pogrupować wyniki po zawodnikach czy po dystansach?")
            self.layout.add_widget(label)

            button_athletes = Button(text='Zawodnicy', on_press=self.on_button_athletes_press)
            button_distances = Button(text='Dystanse', on_press=self.on_button_distances_press)
            button_exit = Button(text='Wyjście', on_press=self.exit_app)
            button_select_another_file = Button(text='Wybierz inny plik', on_press=self.select_another_file)

            self.layout.add_widget(button_athletes)
            self.layout.add_widget(button_distances)
            self.layout.add_widget(button_exit)
            self.layout.add_widget(button_select_another_file)

    def select_another_file(self, instance):
        self.file_chooser.path = '.'  # Otwiera domyślną lokalizację
        self.file_chooser.selection = []  # Czyści wybór pliku
        self.file_path_label.text = ""

        self.layout.clear_widgets()

        self.file_chooser = FileChooserListView(filters=["*.pdf"], path='C:\\')
        select_button = Button(text="Select File", size_hint=(1, None), height=50)
        select_button.bind(on_press=self.display_grouping_options)

        self.file_path_label = Label(text="")

        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(select_button)
        self.layout.add_widget(self.file_path_label)

    def on_button_athletes_press(self, instance):
        self.number = 1
        self.process_choice()

    def on_button_distances_press(self, instance):
        self.number = 2
        self.process_choice()

    def process_choice(self):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0] or ""
        if selected_file:
            text_to_operate_on = PDFReader.get_text_from_pdf(selected_file)

            chunks_of_text = []
            one_chunk_of_text = ""

            for text in text_to_operate_on:
                if re.match(r'[\w-]+\s+\w+,\s+\d+\s+', text) or text == text_to_operate_on[-1] or re.match(
                        r'[\w-]+\s+\w+\s+,\s+\d+\s+', text):
                    chunks_of_text.append(one_chunk_of_text)
                    one_chunk_of_text = ""
                one_chunk_of_text += text + "\n"

            output_text = StringGroupingSystem.group_by(StringSelectingSystem.select_important_string(chunks_of_text),
                                                        self.number)
            print(output_text)

            self.display_output(output_text)

    @mainthread
    def display_output(self, output_text):
        self.layout.clear_widgets()

        scroll_view = CustomScrollView(size_hint=(1, 0.9))
        self.layout.add_widget(scroll_view)

        scroll_view.update_output_text(output_text)

        copy_button = Button(text='Kopiuj do schowka', size_hint=(1, None), height=50)
        copy_button.bind(on_press=scroll_view.copy_to_clipboard)
        self.layout.add_widget(copy_button)

        back_button = Button(text='Wróć do menu', size_hint=(1, None), height=50)
        back_button.bind(on_press=self.display_grouping_options)
        self.layout.add_widget(back_button)

    def exit_app(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="Czy na pewno chcesz wyjść?"))
        yes_button = Button(text="Tak", size_hint=(1, None), height=50)
        no_button = Button(text="Nie", size_hint=(1, None), height=50)

        def close_app(instance):
            App.get_running_app().stop()

        def dismiss_popup(instance):
            popup.dismiss()

        yes_button.bind(on_press=close_app)
        no_button.bind(on_press=dismiss_popup)

        content.add_widget(yes_button)
        content.add_widget(no_button)

        popup = Popup(title="Wyjście", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    PDFParserApp().run()

