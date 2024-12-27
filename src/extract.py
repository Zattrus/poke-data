import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def fetch_pokemon_data(limit=100, offset=0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    response.raise_for_status()
    pokemon_list = response.json().get("results", [])
    
    data = []
    for pokemon in pokemon_list:
        details = requests.get(pokemon["url"]).json()
        data.append({
            "ID": details["id"],
            "Nome": details["name"].title(),
            "Experiência Base": details["base_experience"],
            "Tipos": [t["type"]["name"].title() for t in details["types"]],
            "HP": next(s["base_stat"] for s in details["stats"] if s["stat"]["name"] == "hp"),
            "Ataque": next(s["base_stat"] for s in details["stats"] if s["stat"]["name"] == "attack"),
            "Defesa": next(s["base_stat"] for s in details["stats"] if s["stat"]["name"] == "defense"),
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = fetch_pokemon_data()
    print(df.head())
