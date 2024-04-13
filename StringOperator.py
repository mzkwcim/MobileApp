class StringOperator:
    @staticmethod
    def is_personal_best(text):
        text = int(str(text).replace('%', ""))
        return "r.ż." if text != "-" and text > 99 else ""

    @staticmethod
    def to_title_string(fullname):
        words = fullname.split(' ')
        words = [word.capitalize() for word in words]
        return " ".join(words).replace(",", "")

    @staticmethod
    def arabic_to_romanian_numbers(arabic_number):
        romanian_number = ""
        arabic_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanian_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(arabic_values)):
            while arabic_number >= arabic_values[i]:
                romanian_number += romanian_symbols[i]
                arabic_number -= arabic_values[i]
        return romanian_number
