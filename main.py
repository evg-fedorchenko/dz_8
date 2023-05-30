import collections
from datetime import datetime, timedelta, date

users_list = [
    {
        "nickname": "Bill",
        "birthday": datetime(year=2020, month=1, day=7),
    },
    {
        "nickname": "Jill",
        "birthday": datetime(year=2021, month=5, day=31),
    },
    {
        "nickname": "Kim",
        "birthday": datetime(year=2015, month=6, day=3),
    },
    {
        "nickname": "Lui",
        "birthday": datetime(year=2015, month=6, day=4),
    },
    {
        "nickname": "Jan",
        "birthday": datetime(year=1978, month=9, day=21),
    }
]

d1 = datetime.today().date()
d2 = d1 + timedelta(days=7)

User = collections.namedtuple("User", ["nickname", "birthday"])


def get_birthdays_per_week(users):
    results = {}
    for single_user in users:
        user = User(**single_user)
        bd: date = user.birthday.replace(year=d1.year).date()

        if d1 < bd <= d2:
            day_of_week = bd.weekday()
            day_name = bd.strftime('%A')

            if bd.weekday() in [5, 6]:
                day_of_week = 6
                day_name = "Monday"

            key = (day_of_week, day_name)
            if not results.get(key):
                results[key] = []

            results[key].append(user.nickname)

    for day_of_week, nickname in results.items():
        print(f"{day_of_week[1]}: {', '.join(nickname)}")


if __name__ == "__main__":
    get_birthdays_per_week(users_list)
