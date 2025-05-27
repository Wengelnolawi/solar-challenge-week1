# app/utils.py

import pandas as pd

def load_clean_data(country: str) -> pd.DataFrame:
    """
    Load cleaned data for a given country.
    Args:
        country (str): "benin", "togo", or "sierra_leone"
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    path = f"data/{country.lower()}_clean.csv"
    return pd.read_csv(path)

def get_country_stats(df: pd.DataFrame, country: str) -> dict:
    return {
        "country": country.title(),
        "ghi_mean": df["GHI"].mean(),
        "dni_mean": df["DNI"].mean(),
        "dhi_mean": df["DHI"].mean(),
    }
