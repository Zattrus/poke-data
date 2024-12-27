import pandas as pd

def generate_report(df, stats, top_pokemon):
    with pd.ExcelWriter("pokemon_report.xlsx") as writer:
        top_pokemon.to_excel(writer, sheet_name="Top Pokémon")
        stats.to_excel(writer, sheet_name="Médias por Tipo")
    print("Relatório gerado com sucesso!")

if __name__ == "__main__":
    df = pd.read_csv("pokemon_data.csv")
    stats = calculate_stats(df)
    top_pokemon = df.nlargest(5, "Experiência Base")
    generate_report(df, stats, top_pokemon)
