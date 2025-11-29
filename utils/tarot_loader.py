import pandas as pd

def load_tarot_csv(path="tarot_cards.csv"):
    df = pd.read_csv(path)
    return df.to_dict(orient="records")
