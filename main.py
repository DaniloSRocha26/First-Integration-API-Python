import requests 

def fetch_data(endpoint):
    url = f"https://pokeapi.co/api/v2/{endpoint}"
    response = requests.get(url)

    return response.json() if response.status_code == 200 else None


pokemon = fetch_data("pokemon/pikachu")

if pokemon:
    print(pokemon)
else:
    print("Failed to fetch data")

    