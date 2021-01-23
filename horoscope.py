import requests
from pprint import pprint

zodiac_signs = [
    'aquarius', 'pisces', 'aries', 
    'taurus', 'gemini', 'cancer',
    'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn'
]

print('Welcome to daily horoscope')
sign = input('Please enter your zodiac sign: ').lower()

if sign in zodiac_signs:
    day = "today"
    api_url = "https://aztro.sameerkumar.website/?sign="+sign+"&day="+day
    json = requests.post(api_url).json()
    print(
        '{} horoscope for {}:\n{}\nYou are {}\nYour lucky number for today is {}\n'.format(
            json['current_date'],
            sign,
            json['description'],
            json['mood'].lower(),
            json['lucky_number']
        )
    )

else:
    print('Invalid zodiac sign')