import PyPDF2
import re


class PDFReader:
    @staticmethod
    def get_text_from_pdf(selected_file):
        text = ""
        with open(selected_file, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_number in range(1, len(pdf_reader.pages) + 1):
                page = pdf_reader.pages[page_number - 1]
                text += page.extract_text()

        print(text.split('\n')[1])

        start_index = text.find("KS Posnania Poznań")
        end_index = text.find("KS Warta Poznań")
        converted_text = re.sub(r' - Strona \d+', '', text[start_index:end_index])
        result_strings = re.split(r'\n', converted_text)
        return result_strings
