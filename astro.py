from datetime import datetime, date
import textwrap
import requests
import pandas as pd

ZODIAC_BOUNDARIES = [
    ((1, 20), "Aquarius"), ((2, 19), "Pisces"),
    ((3, 21), "Aries"),    ((4, 20), "Taurus"),
    ((5, 21), "Gemini"),   ((6, 21), "Cancer"),
    ((7, 23), "Leo"),      ((8, 23), "Virgo"),
    ((9, 23), "Libra"),    ((10, 23), "Scorpio"),
    ((11, 22),"Sagittarius"), ((12, 22), "Capricorn"),
    ]

def zodiac_sign(bday: date) -> str:
    m, d = bday.month, bday.day
    for (month, day), sign in ZODIAC_BOUNDARIES:
        if (m, d) < (month, day):
            return prev_sign
        prev_sign = sign
    return "Capricorn"

def get_horoscope(sign: str,
                  day: str = "TODAY",
                  period: str = "daily") -> str:
    base = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope"
    url = f"{base}/{period}"
    params = {"sign": sign.lower(), "day": day.upper()}
    r = requests.get(url, params=params, timeout=5)
    r.raise_for_status()
    return r.json()["data"]["horoscope_data"]

records = []

while True:
    name_in = input("Name (Type your name): ").strip()
    if not name_in:
        break
    birth_str = input("Type your date of birth (YYYY-MM-DD): ").strip()
    try:
        birth_dt = datetime.strptime(birth_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format - try again.")
        continue

    sign = zodiac_sign(birth_dt)
    text = get_horoscope(sign, "TODAY")

    print(f"\n{name_in} \u21D2 {sign}\n" + "-"*40)
    print(textwrap.fill(text, width=72), "\n")

    records.append(
        {"name": name_in,
         "date of birth": birth_dt.isoformat(),
         "zodiac": sign,
         "horoscope": text}
    )

if records:
    df = pd.DataFrame(records)
    df["horoscope"] = df["horoscope"].str.wrap(72)
    df["horoscope"] = "\n" + df["horoscope"]
    df = df.rename(
        columns={
            "name": "name",
            "birthdate": "date of birth",
            "zodiac": "zodiac",
            "horoscope": "horoscope"
        })

    df.to_csv("zodiac_results.csv", index=False)

    print("Saved CSV with wrapped text.")
