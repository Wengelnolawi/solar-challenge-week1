# app/main.py

import streamlit as st
import pandas as pd
import plotly.express as px
from app.utils import load_clean_data, get_country_stats

st.set_page_config(page_title="Solar Analytics Dashboard", layout="wide")

st.title("☀️ Solar Potential Dashboard")
st.markdown("Compare GHI, DNI, and DHI across West African countries.")

# Country selector
countries = ["benin", "togo", "sierra_leone"]
selected = st.multiselect("Select Countries", countries, default=countries)

# Load & Display
if selected:
    all_dfs = []
    stats = []

    for country in selected:
        df = load_clean_data(country)
        df["country"] = country.title()
        all_dfs.append(df)
        stats.append(get_country_stats(df, country))

    combined_df = pd.concat(all_dfs, ignore_index=True)
    stats_df = pd.DataFrame(stats)

    st.subheader("📊 GHI, DNI, and DHI Distribution")
    for metric in ["GHI", "DNI", "DHI"]:
        fig = px.box(combined_df, x="country", y=metric, color="country", title=f"{metric} by Country")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("📋 Summary Statistics")
    st.dataframe(stats_df.style.format("{:.2f}"))
else:
    st.info("Please select at least one country to visualize.")
