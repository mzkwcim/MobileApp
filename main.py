from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from PDFReader import PDFReader
from StringGroupingSystem import StringGroupingSystem
from StringSelectingSystem import StringSelectingSystem
import re

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
        # Tutaj przekazujemy self.number do metody group_by
        text_to_operate_on = PDFReader.get_text_from_pdf()  # Ta metoda musi być zaimplementowana
        chunks_of_text = []
        one_chunk_of_text = ""

        for text in text_to_operate_on:
            if re.match(r'\w+\s+\w+,\s+\d+\s+', text) or text == text_to_operate_on[-1]:
                chunks_of_text.append(one_chunk_of_text)
                one_chunk_of_text = ""
            one_chunk_of_text += text + "\n"

        # Wywołanie odpowiednich metod dla grupowania i wybierania ważnych łańcuchów
        StringGroupingSystem.group_by(StringSelectingSystem.select_important_string(chunks_of_text), self.number)

if __name__ == "__main__":
    MainApp().run()
