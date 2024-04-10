class StringGroupingSystem:
    @staticmethod
    def group_by(competition, number):
        output_text = ""

        if number == 1:
            athlete_name = ""
            for start in competition:
                rest = " ".join(start.split()[2:])
                current_athlete_name = " ".join(start.split()[0:2])
                if athlete_name != current_athlete_name:
                    athlete_name = current_athlete_name
                    output_text += f"{athlete_name}\n{rest}\n"
                else:
                    output_text += f"{rest}\n"
        else:
            grouped_by_distance = {}
            for s in competition:
                distance_key = StringGroupingSystem.get_distance_key(s)
                if distance_key in grouped_by_distance:
                    grouped_by_distance[distance_key].append(s)
                else:
                    grouped_by_distance[distance_key] = [s]

            for distance, strings in grouped_by_distance.items():
                output_text += f"{distance}\n"
                for string in strings:
                    output_text += f"{' '.join(string.split(' ')[:2] + string.split(' ')[4:]).strip()}\n"
                output_text += "\n"
        return output_text
    @staticmethod
    def get_distance_key(string):
        return " ".join(string.split()[2:4])
