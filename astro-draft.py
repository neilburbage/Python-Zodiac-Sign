import requests
# get parameters from the user

# get their sign (Aquarius, Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn.)

sign = input("please enter your zodiac sign: ")
# Get the horoscope day (today, tomorrow, or yesterday)

day = input("Please enter the horoscope day (today, tomorrow, or yesterday): ")

# parameters for the HTTP request

params = (
    ('sign', sign),
    ('day', day)

    )
# make the request
response = requests.post('https://aztro.sameerkumar.website/', params=params)

print(response.json())