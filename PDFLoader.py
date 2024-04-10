from PDFReader import PDFReader
from StringSelectingSystem import StringSelectingSystem
import re


def load_pdf(self, instance, selection, touch):
    if selection:
        file_path = selection[0]
        text_to_operate_on = PDFReader.get_text_from_pdf(file_path)
        chunks_of_text = []
        one_chunk_of_text = ""

        for text in text_to_operate_on:
            if re.match(r'[\w-]+\s+\w+,\s+\d+\s+', text) or text == text_to_operate_on[-1] or re.match(
                    r'[\w-]+\s+\w+\s+,\s+\d+\s+', text):
                chunks_of_text.append(one_chunk_of_text)
                one_chunk_of_text = ""
            one_chunk_of_text += text + "\n"

        output_text = StringSelectingSystem.select_important_string(chunks_of_text)
        self.show_output_popup(output_text)
