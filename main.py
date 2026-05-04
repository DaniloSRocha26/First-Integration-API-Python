import requests 

def fetch_data(endpoint):
    url = f"https://pokeapi.co/api/v2/{endpoint}"
    response = requests.get(url)

    return response.json() if response.status_code == 200 else None

user_pokemon = input("Digite o nome de um pokemon: ")


pokemon = fetch_data(f"pokemon/{user_pokemon}")


if pokemon:
    print(pokemon)
else:
    print("Failed to fetch data")

    