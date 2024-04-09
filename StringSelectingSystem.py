import re
from StringOperator import StringOperator  # Załóżmy, że istnieje moduł string_operator zdefiniowany gdzieś indziej
from unidecode import unidecode


class StringSelectingSystem:
    @staticmethod
    def select_important_string(chunks_of_text):
        adder = 0
        competition = []
        name = ""

        for chunk in chunks_of_text:
            for c in chunk.split("\n"):
                #c2 = unidecode(c)
                #print(c2)
                swimming_event = ""
                if re.match(r'[\w-]+\s+\w+,\s+', c) or re.match(r'\d+\w\s', c) or re.match(r'[\w-]+\s+\w+\s+,\s+', c):
                    distance = re.sub(r'%.+', '', c).split(" ")
                    if '%' in c:
                        swimming_event = f"{distance[0]} {distance[1]}"
                        competition.append(
                            f"{name} {swimming_event} "
                            f"{StringOperator.arabic_to_romanian_numbers(int(distance[5].replace('.', '')))}"
                            f" miejsce {distance[-5]} {StringOperator.is_personal_best(distance[-1])}")
                    elif adder == 0 and '%' not in c:
                        name = StringOperator.to_title_string(c[:c.index(',')])
                    elif len(distance) > 5 and distance[5] != "-":
                        swimming_event = f"{distance[0]} {distance[1]}"
                        competition.append(
                            f"{name} {swimming_event}"
                            f" {StringOperator.arabic_to_romanian_numbers(int(distance[5].replace('.', '')))}"
                            f" miejsce {distance[6]} r.ż.")
                adder += 1
            adder = 0

        return competition
