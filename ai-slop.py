
# python_zodiac_sign/main.py
from datetime import datetime, date
from typing import Dict

# ---------------------------------------------------------------------------
# 1. Sign boundaries (month, day).  The tuple is the first date *inclusive*
#    for each sign; everything < that belongs to the previous sign.
# ---------------------------------------------------------------------------
ZODIAC_BOUNDARIES = [
    ((1, 20),  "Aquarius"),
    ((2, 19),  "Pisces"),
    ((3, 21),  "Aries"),
    ((4, 20),  "Taurus"),
    ((5, 21),  "Gemini"),
    ((6, 21),  "Cancer"),
    ((7, 23),  "Leo"),
    ((8, 23),  "Virgo"),
    ((9, 23),  "Libra"),
    ((10, 23), "Scorpio"),
    ((11, 22), "Sagittarius"),
    ((12, 22), "Capricorn"),
]

def zodiac_sign(birthdate: date) -> str:
    """Return Western zodiac sign for a given birth date."""
    m, d = birthdate.month, birthdate.day
    for (month, day), sign in ZODIAC_BOUNDARIES:
        if (m, d) < (month, day):
            return prev_sign            # found the boundary
        prev_sign = sign               # update previous sign
    return "Capricorn"                 # wrap-around for late Dec / Jan


def describe_person(name: str, birthdate_str: str) -> Dict[str, str]:
    """Parse input, compute zodiac, return a data record."""
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    sign = zodiac_sign(birthdate)
    print(f"{name} (born {birthdate:%d %b %Y}) is a {sign}.")
    return {
        "name": name,
        "birthdate": birthdate.isoformat(),
        "zodiac": sign,
    }


if __name__ == "__main__":
    # — simple manual test —
    record = describe_person("Ada Lovelace", "1815-12-10")
    # ➜ Ada Lovelace (born 10 Dec 1815) is a Sagittarius.
