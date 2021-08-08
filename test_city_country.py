from city_functions import get_city_name

print(" \n  Enter 'q' to quit")

while True:
    city = input(" \n Enter your city name : ")
    if city == 'q':
       break
    country = input("\n Enter your country name : ")
    if country == 'q':
       break
    full_name = get_city_name(city, country)
    print(f" \t Your city address is {full_name}.")
