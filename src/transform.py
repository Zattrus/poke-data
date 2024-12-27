import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def categorize_pokemon(df):
    conditions = [
        (df["Experiência Base"] < 50),
        (df["Experiência Base"].between(50, 100)),
        (df["Experiência Base"] > 100)
    ]
    categories = ["Fraco", "Médio", "Forte"]
    df["Categoria"] = pd.cut(df["Experiência Base"], bins=[-1, 50, 100, float('inf')], labels=categories)
    return df

def count_pokemon_by_type(df):
    all_types = df["Tipos"].explode()
    return all_types.value_counts()

def plot_pokemon_distribution(type_counts):
    sns.barplot(x=type_counts.index, y=type_counts.values)
    plt.title("Distribuição de Pokémon por Tipo")
    plt.xlabel("Tipo")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("pokemon_distribution.png")

def calculate_stats(df):
    df = df.explode("Tipos")
    stats = df.groupby("Tipos")[["HP", "Ataque", "Defesa"]].mean()
    return stats

if __name__ == "__main__":
    df = pd.read_csv("pokemon_data.csv")
    df = categorize_pokemon(df)
    type_counts = count_pokemon_by_type(df)
    plot_pokemon_distribution(type_counts)
    stats = calculate_stats(df)
    print(stats)
