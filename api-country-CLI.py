import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python country_lookup.py <country name>")
    exit()
country = " ".join(sys.argv[1:]).strip()

try:
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url, timeout = 5)
    if response.status_code != 200:
        print("ERROR")
        exit()
    data = response.json()

    country_info = data[0]
    name = country_info["name"]["common"]
    capital = country_info.get("capital", ["N/A"])[0]
    region = country_info.get("region", "N/A")
    population = country_info.get("population", "N/A")

    print("\n" + "=" * 30)
    print("     Country Information")
    print("=" * 30)
    print(f"Name       : {name}")
    print(f"Capital    : {capital}")
    print(f"Region     : {region}")
    print(f"Population : {population}")
    print("=" * 30)
except requests.exceptions.RequestException:
    print("Error: network problem or API unavailable.")


