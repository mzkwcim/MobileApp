import PyPDF2
import re


class PDFReader:
    @staticmethod
    def get_text_from_pdf():
        path = "C:\\users\\mzkwcim\\desktop\\MDMM.pdf"
        text = ""
        with open(path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_number in range(1, len(pdf_reader.pages) + 1):
                page = pdf_reader.pages[page_number - 1]
                text += page.extract_text()

        print("Na starcie " + text.split('\n')[1])

        # W tym fragmencie zastępujemy Regex.Replace używając wyrażeń regularnych Pythona
        # Następnie dzielimy tekst na linie za pomocą '\n' i filtrujemy te, które spełniają nasze kryteria
        # Należy zwrócić uwagę, że to jest przykładowa implementacja, która może wymagać dostosowania
        start_index = text.find("KS Posnania Poznań")
        end_index = text.find("KS Warta Poznań")
        converted_text = re.sub(r' - Strona \d+', '', text[start_index:end_index])
        result_strings = re.split(r'\n', converted_text)
        return result_strings
