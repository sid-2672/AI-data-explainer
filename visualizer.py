# modules/visualizer.py

import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_distributions(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        st.plotly_chart(
            px.histogram(df, x=col, marginal="box", title=f"Distribution of {col}"),
            use_container_width=True
        )

def plot_correlation_matrix(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] > 1:
        corr = numeric_df.corr()
        st.subheader("📊 Correlation Matrix")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)

