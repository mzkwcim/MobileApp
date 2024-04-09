class StringGroupingSystem:
    @staticmethod
    def group_by(competition, number):
        if number == 1:
            athlete_name = ""
            for start in competition:
                rest = " ".join(start.split()[2:])
                current_athlete_name = " ".join(start.split()[0:2])
                if athlete_name != current_athlete_name:
                    athlete_name = current_athlete_name
                    print(f"{athlete_name}\n{rest}")
                else:
                    print(rest)
        else:
            grouped_by_distance = {}
            for s in competition:
                distance_key = StringGroupingSystem.get_distance_key(s)
                if distance_key in grouped_by_distance:
                    grouped_by_distance[distance_key].append(s)
                else:
                    grouped_by_distance[distance_key] = [s]

            for distance, strings in grouped_by_distance.items():
                print(distance)
                for string in strings:
                    print(string)
                print()

    @staticmethod
    def get_distance_key(string):
        return " ".join(string.split()[2:4])
