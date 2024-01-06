from datetime import date
import re
import sys
import inflect

def main():
    birthday = Birthday.get()
    print(birthday.get_minute())


class Birthday:
    def __init__(self, birthday):
        self.birthday = birthday
    
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        if not re.search(r"^\d{4}-\d{2}-\d{2}$", birthday):
            sys.exit("Invalid date")
        self._birthday = birthday
        
    @classmethod
    def get(cls):
        birthday = input("Date of Birth: ").strip()
        return cls(birthday)


    def get_minute(self):
        try:
            input_datetime = date.fromisoformat(self.birthday)
        except Exception:
            sys.exit()
        today_datetime = date.today()
        gap = today_datetime - input_datetime
        minutes = int(gap.total_seconds() / 60)
        # print(int(minutes))
        p = inflect.engine()
        words = p.number_to_words(minutes, andword="")
        return f"{words.capitalize()} minutes"




if __name__ == "__main__":
    main()