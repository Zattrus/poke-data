from src.extract import fetch_pokemon_data
from src.transform import categorize_pokemon, count_pokemon_by_type, plot_pokemon_distribution, calculate_stats
from src.report import generate_report

def main():
    df = fetch_pokemon_data()

    df = categorize_pokemon(df)
    type_counts = count_pokemon_by_type(df)
    stats = calculate_stats(df)

    generate_report(df, stats, df.nlargest(5, "Experiência Base"))
    plot_pokemon_distribution(type_counts)

if __name__ == "__main__":
    main()
